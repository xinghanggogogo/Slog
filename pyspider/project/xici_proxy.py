#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-03-21 09:23:46
# Project: xici_proxy

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    def on_start(self):
        self.crawl('http://www.xicidaili.com/',
                    callback=self.index_page,
                    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
                    )
    # doc和xpath混用.
    def index_page(self, response):
        for each in response.doc('.odd'):    
            res = dict()
            res['ip'] = each.xpath('td')[1].text
            res['port'] = each.xpath('td')[2].text
            print res
