#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-03-13 16:27:52
# Project: 爬取酷狗所有歌手.

from pyspider.libs.base_handler import *
from pyspider.database.mysql.mysqldb import ToMysql

import string

class Handler(BaseHandler):
    crawl_config = {
        'itag': 'v1'
    }

    def on_start(self):
        for tp in range(2, 12):
            for word in string.lowercase:
                for page in range(1, 6):
                    url = 'http://www.kugou.com/yy/singer/index/%s-%s-%s.html' % (page, word, tp)
                    self.crawl(url, callback=self.fetchSinger)

    def fetchSinger(self, response):
        for each in response.doc('.r ul a[href^="http://www.kugou.com/yy/singer/home/"]').items():
            artist = each.attr.title
            kugouid = each.attr.href.split('/', 6)[6].split('.')[0]
            res = dict(artist=artist, kugouid=kugouid)
            yield res

    def on_result(self, res):
        if not res:
            return
        sql = ToMysql()
        sql.insert_singer_meta(**res)
