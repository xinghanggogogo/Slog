#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-11-02 13:41:31

import json
from pyspider.libs.base_handler import *
from pyspider.database.mysql.mysqldb import ToMysql


class Handler(BaseHandler):

    crawl_config = {
    }

    def on_start(self):
        # max=100
        for i in range(1, 2):
            self.crawl('http://www.huya.com/cache.php?m=Live&do=ajaxAllLiveByPage&page=%s&pageNum=1' %i, callback=self.parse_json)

    def parse_json(self, response):
        response = response.json
        res = response['data']['list']
        for item in res:
            save = {
                "room_id" : item['privateHost'],
                 "show_img" : item['screenshot'],
                 "category" : item['gameFullName'],
                 "link" : 'http://www.huya.com/'+item['privateHost'],
                 "title" : item['introduction'],
                 "anchor" : item['nick'],
                 "head_img" : item['avatar180'],
                 "num" : item['totalCount'],
                 "source" : "huya"
            }

            print save
            self.crawl('http://m.huya.com/%s' % item['privateHost'] ,
                      callback=self.get_videolink,
                      save = save,
                      headers={'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16'},
                      fetch_type='js',
                      validate_cert=False
                      )

    def get_videolink(self, response):
        result = response.save
        m3u8_link = response.doc('#video > video > source').attr.src
        print m3u8_link
        result['m3u8_link'] = m3u8_link
        yield result

    def on_result(self, result):
            #print result
            if not result:
                return
            sql = ToMysql()
            sql.into('tvshow',**result)
