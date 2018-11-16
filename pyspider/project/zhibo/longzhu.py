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
        # max=21
        for i in range(1, 2):
            self.crawl('http://api.plu.cn/tga/streams?max-results=50&start-index=%s&sort-by=views&filter=0&game=0' % (i*50), callback=self.parse_json)

    def parse_json(self, response):
            response = response.json
            res = response['data']['items']
            for item in res:
                save = {
                    "room_id" : item['channel']['id'],
                     "show_img" : item['preview'],
                     "category" : item['game'][0]['Name'],
                     "link" : item['channel']['url'],
                     "title" : item['channel']['status'],
                     "anchor" : item['channel']['name'],
                     "head_img" : item['channel']['avatar'],
                     "num" : item['viewers'],
                     "source" : "longzhu"
                }
                self.crawl('http://star.longzhu.com/m/%s' % item['channel']['domain'] ,
                           callback=self.get_videolink,
                           save = save,
                           headers={'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16'},
                           fetch_type='js',
                           validate_cert=False
                           )

    def get_videolink(self, response):
        result = response.save
        m3u8_link = response.doc('#video-player').attr.src
        result['m3u8_link'] = m3u8_link
        yield result

    def on_result(self, result):
            if not result:
                return
            sql = ToMysql()
            sql.into('tvshow',**result)
