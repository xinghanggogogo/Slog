#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-03-17 17:09:21
# Project: 5sings(原唱中国), 通过歌手名搜索伴奏

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from pyspider.libs.base_handler import *
from pyspider.database.mysql.mysqldb import ToMysql

class Handler(BaseHandler):

    crawl_config = {
        'itag': 'bingo'
    }

    sql = ToMysql()

    def on_start(self):
        for page in range(1, 280): # 280
            all_singer = self.sql.get_all_kugou_singer(page)
            for singer in list(all_singer):
                print singer
                key_word = singer['artist'].encode('utf8')
                print key_word
                for page in range(1, 2):
                    self.crawl('http://search.5sing.kugou.com/home/json?keyword=%s&sort=1&page=%s&filter=30&type=0'%('刘德华', 1),
                    callback=self.fetch_meta)

    def fetch_meta(self, response):
        songs_list = response.json['list']
        for item in songs_list:
            song = dict()
            song['name'] = item['originalName']
            song['artist'] = item['originSinger']
            if '<em>' in name:
                name = name.replace('<em>', '')
                name = name.replace('</em>', '')
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
                       #这个UA竟然是必须加的.
                       headers={'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16'},
                       fetch_type='js',
                       #模仿浏览器点击, 拒绝加载音频文件
                       js_script="""
                           $('.pause_btn').click();
                       """,
                       callback=self.fetch_music_ilnk,
                       proxy = '106.75.14.21:80'
                       )

    def fetch_music_ilnk(self, response):
        song = response.save
        music_link = response.doc('audio').attr.src
        duration = response.doc('.middle_time clearfix wsp_allTime > .rt').text()
        song['music_link'] = music_link
        song['duration'] = duration
        print music_link, duration
        #yield song

    def on_result(self, song):
        if not song:
            return
        sql = ToMysql()
        sql.insert_5sing_song_meta(**song)
