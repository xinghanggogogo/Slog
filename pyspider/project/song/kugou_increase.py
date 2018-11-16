#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-03-10 10:39:06
# 酷狗音乐的增量爬取, 通过监视排行榜爬取新歌, 验证krc有效性, 搜索歌曲伴奏

import time
import urllib
import urllib2

from pyspider.libs.base_handler import *
from pyspider.database.mysql.mysqldb import ToMysql

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Handler(BaseHandler):

    crawl_config = {}

    prefix = ['原版', 'KTV', 'ktv']

    def clear_noisy(self, string):
        if '<em>' in string or '</em>' in string:
                string = string.replace('<em>', '')
                string = string.replace('</em>', '')
        return string

    @every()
    def on_start(self):
        self.crawl('http://www.kugou.com/yy/rank/home/', callback=self.fetch_rank_type)

    # 获取排行榜id
    def fetch_rank_type(self, response):
        for each in response.doc('div.pc_temp_side a[href^="http://www.kugou.com/yy/rank/home/"]').items():
            type_id_str = each.attr.href[len('http://www.kugou.com/yy/rank/home/'):][:-5]
            id = type_id_str.split('-')[1]
            web_rank_api = 'http://mobilecdn.kugou.com/api/v3/rank/song?ranktype=1&page=1&rankid=%s&pagesize=10' % id
            self.crawl(web_rank_api, callback=self.fetch_song_info_count, save=dict(id=id))

    def fetch_song_info_count(self, response):
        save = response.save
        id = save['id']
        response = response.json
        total = response['data']['total']
        print id, total
        web_rank_api = 'http://mobilecdn.kugou.com/api/v3/rank/song?ranktype=1&page=1&rankid=%s&pagesize=%s' % (id, total)
        self.crawl(web_rank_api, callback=self.fetch_song_info)

    # 获取歌曲meta
    def fetch_song_info(self, response):
        song_list = response.json['data']['info']
        for song in song_list:

            song_title = song['filename'].encode('utf8')
            song_title = self.clear_noisy(song_title)

            song['name'] = song_title.split('-')[1].strip()
            song['artist'] = song_title.split('-')[0].strip()
            key_word = song_title + '伴奏'
            timestmp = str(time.time())[:-3]

            song_bt_api = 'http://songsearch.kugou.com/song_search_v2?keyword=%s&page=1&pagesize=30&userid=-1clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=%s' % (key_word, timestmp)
            self.crawl(song_bt_api, callback=self.get_song_bt, save=song)

    # 获取歌曲背景音乐哈希
    def get_song_bt(self, response):
        song_meta = response.save
        # 入meata库
        res = dict()
        res['title'] = self.clear_noisy(song_meta['filename'].encode('utf8'))
        res['name'] = self.clear_noisy(song_meta['name'].encode('utf8'))
        res['artist'] = self.clear_noisy(song_meta['artist'].encode('utf8'))
        res['remark'] = song_meta['remark'].encode('utf8').strip()
        res['duration'] = song_meta['duration']
        res['size'] = song_meta['filesize']
        res['hash'] = song_meta['hash']
        res['hash320'] = song_meta['320hash']
        res['source'] = 'kuwo'
        res['source_id'] = song_meta['audio_id']
        # 验证krc有效性
        res['krc'] = 'http://mobilecdn.kugou.com/new/app/i/krc.php?keyword=%s&timelength=%s&type=1&cmd=200&hash=%s' % (urllib.quote(res['title']), res['duration'], res['hash'])
        request = urllib2.Request(res['krc'])
        krcfile = urllib2.urlopen(request)
        krcfile = krcfile.read()
        if krcfile:
            res['state'] = 1 if krcfile else 0
        #入meta库
        self.insert_into_meta(res)

        #入伴奏库
        song_bt_list = response.json['data']['lists']
        for bt_song in song_bt_list:
            res = dict()
            res['title'] = self.clear_noisy(bt_song['FileName'].encode('utf8'))
            res['name'] = res['title'].split('-')[1].strip()
            res['artist'] = res['title'].split('-')[0].strip()
            res['remark'] = bt_song['Auxiliary'].encode('utf8').strip()
            res['duration'] = bt_song['Duration']
            res['size'] = bt_song['FileSize']
            res['bitrate'] = bt_song['Bitrate']
            res['label'] = bt_song['SongLabel']
            res['hash'] = bt_song['FileHash'].encode('utf8')
            res['hash320'] = bt_song['SQFileHash'].encode('utf8')
            res['extname'] = bt_song['ExtName'].encode('utf8')
            res['source'] = 'kuwo'
            res['source_id'] = bt_song['Audioid']
            res['krc'] = 'http://mobilecdn.kugou.com/new/app/i/krc.php?keyword=%s&timelength=%s&type=1&cmd=200&hash=%s' % (urllib.quote(res['title']), res['duration'], res['hash'])

            request = urllib2.Request(res['krc'])
            krcfile = urllib2.urlopen(request)
            krcfile = krcfile.read()
            if krcfile:
                res['state'] = 1 if krcfile else 0

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

            if '伴奏' in res['title'] or res['label'] == '伴奏':
                self.insert_into_bt_meta(res)

    # 入meta库
    def insert_into_meta(self, res):
        if not res:
            return
        sql = ToMysql()
        sql.insert_song_meta(**res)

    # 入伴奏库
    def insert_into_bt_meta(self, res):
        if not res:
            return
        sql = ToMysql()
        sql.insert_bt_song_meta(**res)
