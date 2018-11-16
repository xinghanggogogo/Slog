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
        # max=8
        for i in range(1, 2):
            self.crawl('http://www.huajiao.com/category/1000?pageno=%s' % i, callback=self.index_page)
            # self.crawl('http://www.huajiao.com/category/999?pageno=%s' % i, callback=self.index_page)
            # self.crawl('http://www.huajiao.com/category/1001?pageno=%s' % i, callback=self.index_page)
            # self.crawl('http://www.huajiao.com/category/2?pageno=%s' % i, callback=self.index_page)
            # self.crawl('http://www.huajiao.com/category/5?pageno=%s' % i, callback=self.index_page)
            # self.crawl('http://www.huajiao.com/category/1?pageno=%s' % i, callback=self.index_page)
            # self.crawl('http://www.huajiao.com/category/3?pageno=%s' % i, callback=self.index_page)

    def index_page(self, response):

        for each in response.doc('ul.g-list2 > li'):
                save = {
                    "room_id" : each.xpath('div/a/@href')[0].encode('utf8').split('/')[-1],
                     "show_img" : each.xpath('div/a/div[1]/img/@src')[0].encode('utf8'),
                     "category" : '',
                     "link" : each.xpath('div/a/@href')[0].encode('utf8'),
                     "title" : each.xpath('div/a/div[2]/div[1]/text()')[0].encode('utf8'),
                     "anchor" : each.xpath('div/a/div[2]/div[1]/text()')[0].encode('utf8'),
                     "num" : each.xpath('div/a/div[2]/div[2]/span/text()')[0].encode('utf8'),
                     "source" : "huajiao"
                }
                print save
                self.crawl('http://h.huajiao.com/l/index?liveid=%s&userid=&time=&reference=&from=&isappinstalled=&version=&qd=&channel=' % each.xpath('div/a/@href')[0].encode('utf8').split('/')[-1],
                           callback=self.get_videolink,
                           save = save,
                           headers={'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16'},
                           fetch_type='js',
                           validate_cert=False
                           )

    def get_videolink(self, response):
        result = response.save
        m3u8_link = response.doc('.h5_player > video').attr.src
        result['m3u8_link'] = m3u8_link
        yield result

    def on_result(self, result):
            if not result:
                return
            sql = ToMysql()
            sql.into('tvshow',**result)
