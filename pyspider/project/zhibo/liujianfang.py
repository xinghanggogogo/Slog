#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-11-18 15:13:55

from pyspider.libs.base_handler import *
from pyspider.database.mysql.mysqldb import ToMysql
import json

class Handler(BaseHandler):
    crawl_config = {
    }

    def on_start(self):
        for i in range(1, 2):
            self.crawl('http://www.6.cn/getVisitorMoreList.php?&p=%s&size=100' % i, callback=self.parse_json)

    @config(age=10 * 24 * 60 * 60)
    def parse_json(self, response):
        response = response.json
        res = response['content']['data']
        for item in res:
            save = {
                "room_id" : item['rid'],
                 "show_img" : item['pic'],
                 "category" : '',
                 "link" : 'http://v.6.cn/%s' % item['rid'],
                 "m3u8_link" : ''
                 "title" : item['username'],
                 "anchor" : item['username'],
                 "num" : item['count'],
                 "source" : "liujianfang"
            }
            yield save
            '''
            print save
            self.crawl('http://m.v.6.cn/%s' % item['rid'],
                      callback=self.get_videolink,
                      save = save,
                      headers={'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16'},
                      fetch_type='js',
                      js_script="""
                           function() {
                               setTimeout("window.location.reload()", 1000);
                           }""",
                      validate_cert=False
                      )
            '''
    def get_videolink(self, response):
        result = response.save
        m3u8_link = response.doc('.player > video').attr.src
        head_img = response.doc('section.top > img').attr.src
        if not head_img:
            result['head_img'] = ''
        if not m3u8_link:
            result['m3u8_link'] = ''
        print result
        #yield result

    def on_result(self, result):
            #print result
            if not result:
                return
            sql = ToMysql()
            sql.into('tvshow',**result)
