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
        self.crawl('http://www.yy.com/mobileweb/play/live?sid=22490906&ssid=22490906#!/live/room', callback=self.get_videolink)
        #for i in range(1,2):
            #self.crawl('http://www.yy.com/more/page.action?biz=dance&subBiz=idx&page=%s&moduleId=313' % i, callback=self.parse_json)
            #self.crawl('http://www.yy.com/more/page.action?biz=sing&subBiz=idx&page=%s&moduleId=308' % i, callback=self.parse_json)
            #self.crawl('http://www.yy.com/more/page.action?biz=talk&subBiz=idx&page=%s&moduleId=328' % i, callback=self.parse_json)
            #self.crawl('http://www.yy.com/more/page.action?biz=mc&subBiz=idx&page=%s&moduleId=322' % i, callback=self.parse_json)
            #self.crawl('http://www.yy.com/more/page.action?biz=red&subBiz=idx&page=%s&moduleId=102' % i, callback=self.parse_json)
            #self.crawl('http://www.yy.com/more/page.action?biz=sport&subBiz=idx&page=%s&moduleId=28' % i, callback=self.parse_json)
            #self.crawl('http://www.yy.com/more/page.action?biz=game&subBiz=idx&page=%s&moduleId=260' % i, callback=self.parse_json)
            #self.crawl('http://www.yy.com/more/page.action?biz=mgame&subBiz=idx&page=%s&moduleId=256' % i, callback=self.parse_json)
            #self.crawl('http://www.yy.com/more/page.action?biz=other&subBiz=idx&page=%s&moduleId=65' % i, callback=self.parse_json)


    def parse_json(self, response):
            res = response.json['data']['data']
            for item in res:
                link = item['liveUrl'].split('?')[0]
                save = {
                    "room_id" : item['sid'],
                     "show_img" : item['thumb'],
                     "category" : '',
                     "link" : link,
                     "title" : item['desc'],
                     "anchor" : item['name'],
                     "num" : item['users'],
                     "source" : "yy"
                }

                self.crawl('http://www.yy.com/mobileweb/play/live?sid=%s&ssid=%s#!/live/room' % (item['sid'],item['ssid']),
                           callback=self.get_videolink,
                           save = save,
                           headers={'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16'},
                           fetch_type='js',
                           js_script="""function() {setTimeout("", 10000);}""",
                           validate_cert=False
                           )

    def get_videolink(self, response):
        result = response.save
        m3u8_link = response.doc('#player').attr.src
        head_img = response.doc('.anchor-icon').attr.style.split('url')[1][2:-3]
        result['head_img'] = head_img
        result['m3u8_link'] = m3u8_link
        yield result

    def on_result(self, result):
            if not result:
                return
            sql = ToMysql()
            sql.into('tvshow',**result)
