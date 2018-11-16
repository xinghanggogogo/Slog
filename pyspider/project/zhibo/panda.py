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
        for i in range(1, 2):
            self.crawl('http://www.panda.tv/live_lists?status=2&order=person_num&pageno=%s&pagenum=120' % i, callback=self.parse_json)

    def parse_json(self, response):
        response = response.json
        res = response['data']['items']
        for item in res:
            save = {
                "room_id" : item['id'],
                 "show_img" : item['pictures']['img'],
                 "category" : item['classification']['cname'],
                 "link" : 'http://www.panda.tv/%s'+item['id'],
                 "m3u8_link": '',
                 "title" : item['name'],
                 "anchor" : item['userinfo']['nickName'],
                 "head_img" : item['userinfo']['avatar'],
                 "num" : item['person_num'],
                 "source" : "panda"
            }
            yield save

            '''
            print save
            self.crawl('http://m.panda.tv/room.html?roomid=%s&psrc=pc_client-baidubox-shouye' % item['id'],
                      callback=self.get_videolink,
                      save = save,
                      headers={'User-Agent': ''},
                      fetch_type='js',
                      validate_cert=False
                      )
            '''

    def get_videolink(self, response):
        result = response.save
        m3u8_link = response.doc('#video > video').attr.src
        result['m3u8_link'] = m3u8_link
        yield result

    def on_result(self, result):
            if not result:
                return
            sql = ToMysql()
            sql.into('tvshow',**result)
