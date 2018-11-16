#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-03-27 13:03:58
# Project: 5sing(原唱中国), 通过歌曲名称(通过es搜索引擎获取)调用搜索接口, 补全meta

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from pyspider.libs.base_handler import *
from pyspider.database.mysql.mysqldb import ToMysql

from pyelasticsearch import ElasticSearch
es = ElasticSearch('http://localhost:9200')
import re

class Handler(BaseHandler):

    crawl_config = {
        'itag': 'bingoorange'
    }

    sql = ToMysql()
    UA_M = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16'

    def on_start(self):
        for _id in range(1, 10):   # 2877025
            song = self.sql.get_meta(_id)
            song = song[0]
            # 过滤伴奏:
            if '伴奏' in song['name'] or song['label'] == '伴奏':
                continue
            # 通过es获取歌名`歌手`时长
            name = song.get('name')
            # 去噪声
            if '<em>' in name:
                name = name.replace('<em>', '')
                name = name.replace('</em>', '')
                print('name: '+name)
            name = re.sub(r'\(.*\)', '', name)
            name = re.sub(r'\[.*\]', '', name)
            print name

            self.crawl('http://search.5sing.kugou.com/home/json?keyword=%s&sort=1&page=%s&filter=30&type=0'%(name, 1), callback=self.fetch_meta)

    def fetch_meta(self, response):
        songs_list = response.json['list']
        for item in songs_list:
            song = dict()
            song['name'] = item['originalName']
            song['artist'] = item['originSinger']
            if '>' in song['artist']:
                song['artist'] = song['artist'].split('>')[1][:-len('</em>')+1]
            song['extname'] = item['ext']
            song['label'] = item['typeName']
            song['size'] = item['songSize']
            song['song_url'] = item['songurl']
            song['download_url'] = item['downloadurl']
            song['source_id'] = item['songId']
            song['addtime'] = item['createTime']
            song['source'] = '5sing'
            song['super_json'] = str(item)
            fetch_music_link = item['songurl']

            self.crawl(fetch_music_link,
                       save=song,
                       headers={'User-Agent': self.UA_M},
                       callback=self.fetch_music_ilnk
                       )

    def fetch_music_ilnk(self, response):

        song = response.save
        music_link = response.doc('audio').attr.src
        song['music_link'] = music_link
        print music_link
        yield song

    def on_result(self, song):
        if not song:
            return
        self.sql.insert_5sing_song_meta(**song)
