#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-06-04 08:35:11
# Project: kugou_album_api

from pyspider.libs.base_handler import *
from pyspider.database.mysql.mysqldb import ToMysql

import re
import json
import time
import urllib
import urllib2

class Handler(BaseHandler):

    crawl_config = {
         'itag': 'thunderLabBeginingv1'
    }

    def clear_noisy(self, string):
        if '<em>' in string or '</em>' in string:
                string = string.replace('<em>', '')
                string = string.replace('</em>', '')
        return string

    @every(minutes=3 * 60)
    def on_start(self):
        path = 'http://mobilecdnbj.kugou.com/api/v3/album/list?'
        for page in range(1, 3):
            for _type in range(1, 4):
                uri = 'withpriv=1&sorttype=1&version=8800&apiver=1&plat=0&page=%s&type=%s&pagesize=50&with_res_tag=1' % (page, _type)
                self.crawl(path+uri, callback=self.index_page, save={'tp': _type})

    @config(age=10)
    def index_page(self, response):
        tp = response.save['tp']
        response = response.content
        response = re.search(r'-->(.*)<!--', response).group(1)
        response = json.loads(response)
        album_list = response['data']['info']
        print album_list
        for album in album_list:
            print album['albumid']
            album_api = 'http://mobileservice.kugou.com/api/v3/album/song?albumid=%s&plat=0&page=1&pagesize=-1&version=8800&with_res_tag=1' % album['albumid']
            self.crawl(album_api, callback=self.album_page, save={'tp': tp, 'album_id': album['albumid'] })

    @config(age=10)
    def album_page(self, response):
        language = response.save['tp']
        album_id = response.save['album_id']
        response = response.content
        response = re.search(r'-->(.*)<!-', response).group(1)
        response = json.loads(response)
        song_list = response['data']['info']
        print song_list
        for song in song_list:
            res = dict()
            res['title'] = self.clear_noisy(song['filename'].encode('utf8'))
            res['name'] = res['title'].split('-', 1)[1].strip() if '-' in res['title'] else res['title']
            res['artist'] = res['title'].split('-')[0].strip() if '-' in res['title'] else ''
            res['remark'] = song['remark'].encode('utf8').strip()
            res['duration'] = song['duration']
            res['size'] = song['filesize']
            res['bitrate'] = song['bitrate']
            res['label'] = ''
            res['hash'] = song['hash'].encode('utf8')
            res['hash320'] = song['320hash'].encode('utf8')
            res['extname'] = song['extname'].encode('utf8')
            res['source'] = 'kuwo'
            res['source_id'] = song['audio_id']
            res['krc'] = 'http://mobilecdn.kugou.com/new/app/i/krc.php?keyword=%s&timelength=%s&type=1&cmd=200&hash=%s' % (urllib.quote(res['title']), res['duration'], res['hash'])

            request = urllib2.Request(res['krc'])
            krcfile = urllib2.urlopen(request)
            krcfile = krcfile.read()
            res['state'] = 1 if krcfile else 0
            res['language'] = language
            res['album_id'] = album_id

            print res['title']
            print res['name']
            print res['artist']
            print res['remark']
            print res['duration']
            print res['size']
            print res['bitrate']
            print res['label']
            print res['hash']
            print res['hash320']
            print res['krc']
            print res['source']
            print res['source_id']
            print res['state']
            print res['language']
            print res['album_id']

            self.insert_into_meta(res)

    # 入meta库
    def insert_into_meta(self, res):
        print res
        if not res:
            return
        sql = ToMysql()
        sql.insert_song_meta(**res)
