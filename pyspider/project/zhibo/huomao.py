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
        for i in range(1, 4):
            self.crawl('http://www.huomao.com/channels/channel.json?page=%s&page_size=10&cache_time=1477987230&game_url_rule=all' % i, callback=self.parse_json)

    def parse_json(self, response):
        response = response.json
        res = response['data']['channelList']
        for item in res:
            save = {
                "room_id" : item['room_number'],
                 "show_img" : item['image'],
                 "category" : item['gameCname'],
                 "link" : 'http://www.huomao.com/'+item['room_number'],
                 "title" : item['channel'],
                 "anchor" : item['nickname'],
                 "head_img" : item['headimg']['big'],
                 "num" : item['originviews'],
                 "source" : "huomao"
            }
            self.crawl('http://m.huomao.com/mobile/mob_live/%s' % item['room_number'] ,
                       callback=self.get_videolink,
                       save = save,
                       headers={'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16'},
                       fetch_type='js',
                       validate_cert=False
                       )

    def get_videolink(self, response):
        result = response.save
        m3u8_link = response.doc('.vedio > video > source').attr.src
        result['m3u8_link'] = m3u8_link
        yield result

    def on_result(self, result):
            if not result:
                return
            sql = ToMysql()
            sql.into('tvshow',**result)
