#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-03-25 13:56:04
# Project: test_phantomjs

from pyspider.libs.base_handler import *
from pyquery import PyQuery

class Handler(BaseHandler):

    UA_M = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'

    crawl_config = {
    }

    def on_start(self):
        self.crawl('http://5sing.kugou.com/bz/440943.html',
                    headers={'User-Agent': self.UA_M},
                    fetch_type='js',
                    callback=self.index)

    def index(self, response):
        response = PyQuery(response.doc)
        print response("player").attr.src
