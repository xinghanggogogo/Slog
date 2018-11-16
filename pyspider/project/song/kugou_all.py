#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-03-11 15:35:47
# Project: 搜索接口爬取歌手的歌曲做酷狗的全量爬取, 总计300万

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from pyspider.libs.base_handler import *
from pyspider.database.mysql.mysqldb import ToMysql

import time


class Handler(BaseHandler):

    sql = ToMysql()

    crawl_config = {
        'itag': 'v123'
    }

    def on_start(self):
        for page in range(1, 280):
            all_singer = self.sql.get_all_kugou_singer(page)
            for singer in list(all_singer):
                print singer
                key_word = singer['artist'].encode('utf8')
                print key_word
                timestmp = str(time.time())[:-3]
                for page in range(1, 5):
                    song_search_api = 'http://songsearch.kugou.com/song_search_v2?keyword=%s&page=%s&pagesize=200&userid=-1clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=%s' % (key_word, page, timestmp)
                    print song_search_api
                    self.crawl(song_search_api, callback=self.get_song_bthash)

    def get_song_bthash(self, response):
        song_list = response.json['data']['lists']
        for song in song_list:
            # 这里是37行
            res = dict()
            res['title'] = song['FileName'].encode('utf8')
            res['name'] = song['FileName'].encode('utf8').split('-', 1)[1].strip()
            if not res['name']:
                res['name'] = res['title']
            res['artist'] = song['FileName'].encode('utf8').split('-', 1)[0].strip()
            if '<em>' in res['artist']:
                res['artist'] = res['artist'].replace('<em>', '')
                res['artist'] = res['artist'].replace('</em>', '')
            res['remark'] = song['Auxiliary'].encode('utf8').strip()
            res['duration'] = song['Duration']
            res['size'] = song['FileSize']
            res['bitrate'] = song['Bitrate']
            res['label'] = song['SongLabel']
            # 搜索接口并没有提供addtime
            res['hash'] = song['FileHash'].encode('utf8')
            res['320hash'] = song['SQFileHash'].encode('utf8')
            res['extname'] = song['ExtName'].encode('utf8')
            res['source'] = 'kuwo'
            res['source_id'] = song['Audioid']
            res['super_json'] = str(song)
            res['krc'] = 'http://mobilecdn.kugou.com/new/app/i/krc.php?keyword=%s&timelength=301000&type=1&cmd=200&hash=%s' % (res['title'], res['hash'])

            print res['title']
            print res['name']
            print res['artist']
            print res['remark']
            print '时长: '+str(res['duration'])
            print '大小: '+str(res['size'])
            print 'hash: '+res['hash']
            print '320hash: '+res['320hash']
            print res['extname']
            print '比特率: '+str(res['bitrate'])
            print res['krc']
            print res['source']
            print res['source_id']
            print res['super_json']

            yield res

    # 入库
    def on_result(self, res):
        if not res:
            return
        sql = ToMysql()
        sql.insert_song_meta(**res)
