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
        for i in range(1, 2):
            self.crawl('http://www.quanmin.tv/json/play/list.json', callback=self.parse_json)

    def parse_json(self, response):
            response = response.json
            res = response['data']
            for item in res:
                yield {
                    "room_id" : item['uid'],
                     "show_img" : item['thumb'],
                     "category" : item['category_name'],
                     "link" : 'http://www.quanmin.tv/v/'+item['uid'],
                     "m3u8_link": 'http://hls.quanmin.tv/live/%s_L3/playlist.m3u8' % item['uid'],
                     "video_link": "http://www.quanmin.tv/yileyou/%s" % item['uid'],
                     "title" : item['title'],
                     "anchor" : item['nick'],
                     "head_img" : item['avatar'],
                     "num" : item['view'],
                     "source" : "quanmin"
                }

    def on_result(self, result):
            if not result:
                return
            sql = ToMysql()
            sql.into('tvshow',**result)
