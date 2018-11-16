#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-11-29 10:14:21
# Project: tvshow_hotissue

from pyspider.libs.base_handler import *
from pyspider.database.mysql.mysqldb import ToMysql
import hashlib


class Handler(BaseHandler):
    crawl_config = {
    }

    def on_start(self):
        self.crawl('http://www.15w.com/xinwen/index_1.html', callback=self.parse_page)
        self.crawl('http://www.15w.com/xinwen/index_2.html', callback=self.parse_page)

    def parse_page(self, response):
        for each in response.doc('div.mode-box'):
            title = each.xpath('div/a/text()')[0].encode('utf8')
            img = each.xpath('a/img/@src')[0].encode('utf8')
            description = each.xpath('div/p/text()')[0].encode('utf8')
            link = each.xpath('div/a/@href')[0].encode('utf8')
            source = '15W'
            md5 = hashlib.md5(img+link+source).hexdigest()

            print title
            print img
            print description
            print link
            print img
            print source
            print md5
            print ''

            yield {
                'title':title,
                'img':img,
                'description':description,
                'link':link,
                'img':img,
                'source':source,
                'md5':md5
            }

    def on_result(self, result):
        if not result:
            return
        sql = ToMysql()
        sql.into_issue('hotissue',**result)
