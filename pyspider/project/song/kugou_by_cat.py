#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-04-12 17:57:20
# Project: kugou_app_cat
# 爬取对象为酷狗手机app, 通过charles实现代理, 爬取酷狗音乐所有带有标签的歌曲, 共计550000

from pyspider.libs.base_handler import *
from pyspider.database.mysql.mysqldb import ToMysql

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import re
import json

class Handler(BaseHandler):
    crawl_config = {
    }

    # 首页api
    def on_start(self):
        self.crawl('http://mobilecdnbj.kugou.com/api/v3/tag/list?apiver=2&plat=0&pid=0', callback=self.index_api)

    def index_api(self, response):
        response = response.json
        indexes = response['data']['info']
        for item in indexes:
            index = item['name']
            index_id = item['id']
            cats = item['children']
            for item in cats:
                cat = item['name']
                cat_id = item['id']
                has_child = item['has_child']
                res = dict(index=index, index_id=index_id, cat=cat, cat_id=cat_id)

                print 'index: ' + res.get('index')
                print 'index_id: ' + str(res.get('index_id'))
                print 'cat: ' + res.get('cat')
                print 'cat_id: ' + str(res.get('cat_id'))
                print 'has_child: ' + str(item.get('has_child'))
                print ''

                if has_child:
                    self.crawl('http://mobilecdnbj.kugou.com/api/v3/tag/list?apiver=2&plat=0&pid=%s' % cat_id, save=res, callback=self.cat_parse)
                else:
                    self.crawl('http://mobilecdnbj.kugou.com/api/v3/tag/info?&apiver=2&id=%s' % cat_id, save=res, callback=self.cat_parse_no_child)

    def cat_parse(self, response):
        res = response.save
        response = response.json
        modules = response['data']['info']
        for module in modules:
            tags = module['children']
            for tag_item in tags:

                _res = dict()
                _res['index'] = res['index']
                _res['index_id'] = res['index_id']
                _res['cat'] = res['cat']
                _res['cat_id'] = res['cat_id']
                _res['tag'] = tag_item['name']
                _res['tag_id'] = tag_item['id']
                _res['song_tag_id'] = tag_item['song_tag_id']
                _res['special_tag_id'] = tag_item['special_tag_id']
                _res['album_tag_id'] = tag_item['album_tag_id']

                if tag_item['song_tag_id']:
                    url = 'http://mobilecdnbj.kugou.com/api/v3/tag/songList?tagid=%s&plat=0&page=1&pagesize=20&version=8708' % _res['song_tag_id']
                    self.crawl(url, save=_res, callback=self.fetch_song_total_count)

                if tag_item['special_tag_id']:
                    url = 'http://mobilecdnbj.kugou.com/api/v3/tag/specialList?tagid=%s&plat=0&sort=2&ugc=1&id=%s&page=1&pagesize=20' % (_res['special_tag_id'], _res['tag_id'])
                    self.crawl(url, save=_res, callback=self.fetch_special_total_count)

                if tag_item['album_tag_id']:
                    url = 'http://mobilecdnbj.kugou.com/api/v3/tag/albumList?tagid=%s&plat=0&sort=2&page=1&pagesize=20&version=8708' % _res['album_tag_id']
                    self.crawl(url, save=_res, callback=self.fetch_album_total_count)

    def cat_parse_no_child(self, response):
        res = response.save
        response = response.json
        data = response['data']

        _res = dict()
        _res['index'] = res['index']
        _res['index_id'] = res['index_id']
        _res['cat'] = res['cat']
        _res['cat_id'] = res['cat_id']
        _res['tag'] = ''
        _res['tag_id'] = data['id']
        _res['song_tag_id'] = data['song_tag_id']
        _res['special_tag_id'] = data['special_tag_id']
        _res['album_tag_id'] = data['album_tag_id']

        if _res['song_tag_id']:
            url = 'http://mobilecdnbj.kugou.com/api/v3/tag/songList?tagid=%s&plat=0&page=1&pagesize=20&version=8708' % _res['song_tag_id']
            self.crawl(url, save=_res, callback=self.fetch_song_total_count)

        if _res['special_tag_id']:
            url = 'http://mobilecdnbj.kugou.com/api/v3/tag/specialList?tagid=%s&plat=0&sort=2&ugc=1&id=%s&page=1&pagesize=20' % (_res['special_tag_id'], _res['tag_id'])
            self.crawl(url, save=_res, callback=self.fetch_special_total_count)

        if _res['album_tag_id']:
            url = 'http://mobilecdnbj.kugou.com/api/v3/tag/albumList?tagid=%s&plat=0&sort=2&page=1&pagesize=20&version=8708' % _res['album_tag_id']
            self.crawl(url, save=_res, callback=self.fetch_album_total_count)

    def fetch_song_total_count(self, response):
        res = response.save
        response = response.json
        total = response['data']['total']
        page_count = (total + 20 - 1) / 20
        print total
        print page_count
        for page in range(1, page_count+1):
            url = 'http://mobilecdnbj.kugou.com/api/v3/tag/songList?tagid=%s&plat=0&page=%s&pagesize=20&version=8708' % (res['song_tag_id'], page)
            print url
            self.crawl(url, callback=self.song_parse, save=res)

    def fetch_special_total_count(self, response):
        res = response.save
        response = response.json
        total = response['data']['total']
        page_count = (total + 20 - 1) / 20
        print total
        print page_count
        for page in range(1, page_count+1):
            url = 'http://mobilecdnbj.kugou.com/api/v3/tag/specialList?tagid=%s&plat=0&sort=2&ugc=1&id=%s&page=%s&pagesize=20' % (res['special_tag_id'], res['tag_id'], page)
            print url
            self.crawl(url, callback=self.special_parse, save=res)

    def fetch_album_total_count(self, response):
        res = response.save
        response = response.json
        total = response['data']['total']
        page_count = (total + 20 - 1) / 20
        print total
        print page_count
        for page in range(1, page_count+1):
            url = 'http://mobilecdnbj.kugou.com/api/v3/tag/albumList?tagid=%s&plat=0&sort=2&page=%s&pagesize=20&version=8708' % (res['album_tag_id'], page)
            print url
            self.crawl(url, callback=self.album_parse, save=res)

    def song_parse(self, response):
        res = response.save
        response = response.json
        songs = response['data']['info']
        for song in songs:
            meta = dict()
            meta['title'] = song['filename']
            meta['name'] = song['filename'].split('-')[1].strip()
            meta['artist'] = song['filename'].split('-')[0].strip()
            meta['extname'] = song['extname']
            meta['size'] = song['filesize']
            meta['size320'] = song['320filesize']
            meta['sizesq'] = song['sqfilesize']
            meta['hash'] = song['hash']
            meta['hash320'] = song['320hash']
            meta['hashsq'] = song['sqhash']
            meta['bitrate'] = song['bitrate']
            meta['duration'] = song['duration']
            meta['source_id'] = song['audio_id']
            meta['_index'] = res['index']
            meta['cat'] = res['cat']
            meta['tag'] = res['tag']

            yield meta


    def special_parse(self, response):
        res = response.save
        response = response.json
        songs_special = response['data']['info']
        for song_special in songs_special:
            specialid = song_special['specialid']
            url = 'http://mobilecdnbj.kugou.com/api/v3/special/song?plat=0&specialid=%s&page=1&pagesize=-1&version=8708&with_res_tag=1' % specialid
            print url
            self.crawl(url, callback=self.get_special_song, save=res)

    def album_parse(self, response):
        res = response.save
        response = response.json
        albums = response['data']['info']
        for album in albums:
            albumid = album['albumid']
            url = 'http://mobilecdnbj.kugou.com/api/v3/album/song?albumid=%s&plat=0&page=1&pagesize=-1&version=8708&with_res_tag=1' % albumid
            print url
            self.crawl(url, callback=self.get_album_song, save=res)

    def get_special_song(self, response):
        res = response.save
        response = str(response.text)
        response = re.search(r'>(.+)<', response).group(1)
        response = json.loads(response)
        songs = response['data']['info']
        for song in songs:
            print song['filename']
            print song['filename'].split('-')[1].strip()
            print song['filename'].split('-')[0].strip()
            print song['extname']
            print song['filesize']
            print song['320filesize']
            print song['sqfilesize']
            print song['hash']
            print song['320hash']
            print song['sqhash']
            print song['bitrate']
            print song['duration']
            print song['audio_id']
            print res['index']
            print res['cat']
            print res['tag']
            print ''

            meta = dict()
            meta['title'] = song['filename']
            meta['name'] = song['filename'].split('-')[1].strip()
            meta['artist'] = song['filename'].split('-')[0].strip()
            meta['extname'] = song['extname']
            meta['size'] = song['filesize']
            meta['size320'] = song['320filesize']
            meta['sizesq'] = song['sqfilesize']
            meta['hash'] = song['hash']
            meta['hash320'] = song['320hash']
            meta['hashsq'] = song['sqhash']
            meta['bitrate'] = song['bitrate']
            meta['duration'] = song['duration']
            meta['source_id'] = song['audio_id']
            meta['_index'] = res['index']
            meta['cat'] = res['cat']
            meta['tag'] = res['tag']

            yield meta

    def get_album_song(self, response):
        res = response.save
        response = str(response.text)
        response = re.search(r'>(.+)<', response).group(1)
        response = json.loads(response)
        songs = response['data']['info']
        for song in songs:

            meta = dict()
            meta['title'] = song['filename']
            meta['name'] = song['filename'].split('-')[1].strip()
            meta['artist'] = song['filename'].split('-')[0].strip()
            meta['extname'] = song['extname']
            meta['size'] = song['filesize']
            meta['size320'] = song['320filesize']
            meta['sizesq'] = song['sqfilesize']
            meta['hash'] = song['hash']
            meta['hash320'] = song['320hash']
            meta['hashsq'] = song['sqhash']
            meta['bitrate'] = song['bitrate']
            meta['duration'] = song['duration']
            meta['source_id'] = song['audio_id']
            meta['_index'] = res['index']
            meta['cat'] = res['cat']
            meta['tag'] = res['tag']

            yield meta

    def on_result(self, res):
        if not res:
            return
        sql = ToMysql()
        sql.insert_kugou_cat_meta(**res)
