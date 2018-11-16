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
        self.crawl('http://webapi.busi.inke.cn/web/live_hotlist_pc', callback=self.parse_json)

    def parse_json(self, response):
        response = response.json
        res = response['data']['hotlists']
        for item in res:
            yield {
                "room_id" : item['liveid'],
                 "show_img" : item['portrait'],
                 "category" : '',
                 "link" : 'http://www.inke.cn/live.html?uid=%s&id=%s' % (item['id'], item['liveid']),
                 "m3u8_link": 'http://pullhls99.a8.com/live/%s/playlist.m3u8' % item['liveid'],
                 "title" : item['title'],
                 "anchor" : item['nick'],
                 "head_img" : item['portrait'],
                 "num" : item['online_users'],
                 "source" : "yingke"
            }

    def on_result(self, result):
            if not result:
                return
            sql = ToMysql()
            sql.into('tvshow',**result)
