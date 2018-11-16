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
        self.crawl('http://open.douyucdn.cn/api/RoomApi/game', callback=self.parse_cat)

    def parse_cat(self, response):
        response = response.json
        res = response['data']
        for item in res:
            self.crawl('http://open.douyucdn.cn/api/RoomApi/live/%s' % item['cate_id'], callback=self.parse_json)

    def parse_json(self, response):
            response = response.json
            res = response['data']
            for item in res:
                yield {
                    "room_id" : item['room_id'],
                    "show_img" : item['room_src'],
                    "category" : item['game_name'],
                    "link" : item['url'],
                    "video_link": 'https://staticlive.douyucdn.cn/common/share/play.swf?room_id=%s' % item['room_id'],
                    "title" : item['room_name'],
                    "anchor" : item['nickname'],
                    "head_img" : item['avatar'],
                    "num" : item['online'],
                    "source" : "douyu"
                }

    def on_result(self, result):
            if not result:
                return
            sql = ToMysql()
            sql.into('tvshow',**result)
