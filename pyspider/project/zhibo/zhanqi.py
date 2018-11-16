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
            self.crawl('https://www.zhanqi.tv/api/static/v2.1/live/list/50/%s.json' % i, callback=self.parse_json)

    def parse_json(self, response):
            response = response.json
            res = response['data']['rooms']

            for item in res:
                video_id = item['videoId']
                yield {
                    "room_id" : item['id'],
                     "show_img" : item['bpic'],
                     "category" : item['gameName'],
                     "link" : 'http://www.zhanqi.tv' + item['url'],
                     "title" : item['title'],
                     "anchor" : item['nickname'],
                     "head_img" : item['avatar']+'-big',
                     "num" : item['online'],
                     "video_link" : 'http://www.zhanqi.tv/live/embed?roomId=%s' % (video_id),
                     "m3u8_link" : 'http://dlhls.cdn.zhanqi.tv/zqlive/%s.m3u8' % (video_id),
                     "source" : "zhanqi"
                }

    def on_result(self, result):
            if not result:
                return
            sql = ToMysql()
            sql.into('tvshow',**result)
