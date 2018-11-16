#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-11-02 13:41:31

from pyspider.libs.base_handler import *
from pyspider.database.mysql.mysqldb import ToMysql
import json


class Handler(BaseHandler):
    crawl_config = {
    }

    def on_start(self):
        # max = 30
        for i in range(1, 2):
            self.crawl('http://live.bilibili.com/area/liveList?area=all&order=online&page=%s' % i, callback=self.parse_json)

    def parse_json(self, response):
            response = response.json
            res = response['data']
            for item in res:
                save = {
                    "room_id" : item['roomid'],
                     "show_img" : item['cover'],
                     "category" : item['areaName'],
                     "link" : 'http://live.bilibili.com' + item['link'],
                     "title" : item['title'],
                     "anchor" : item['uname'],
                     "head_img" : item['face'],
                     "num" : item['online'],
                     "source" : "bzhan"
                }
                self.crawl('http://live.bilibili.com/h5/%s' % item['roomid'] ,
                           callback=self.get_videolink,
                           save = save,
                           headers={'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16'},
                           fetch_type='js',
                           #模仿浏览器点击
                           js_script="""
                               function() {
                                   setTimeout("$('.player-icon').click()", 1000);
                               }""",
                          validate_cert=False
                          )

    def get_videolink(self, response):
        result = response.save
        m3u8_link = response.doc('.player-box > video > source').attr.src
        result['m3u8_link'] = m3u8_link
        print result['m3u8_link']
        #yield result

    def on_result(self, result):
        if not result:
            return
        sql = ToMysql()
        sql.into('tvshow',**result)
