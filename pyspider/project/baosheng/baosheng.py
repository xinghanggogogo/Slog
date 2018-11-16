#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-10-26 16:24:35
# Project: baosheng

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import csv
import re

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
        'itag': 'baosheng3'
    }
    
    # 特色音乐推荐:
    #def on_start(self):
    #    for page in range(1, 4):
    #        self.crawl('http://www.boosoochina.com/tsyytj/news.php?lang=cn&class1=314&page=%s' % page, callback=self.index_page)

    #def index_page(self, response):
    #   for each in response.doc('.list > a[href^="http"]').items():
    #       self.crawl(each.attr.href, callback=self.detail_page)

    #def detail_page(self, response):
    #    res = []
        
    #    for each in response.doc('p strong').items():
    #       res.append(each.text())
    #    res = [[item] for item in res if "《" in item]
    #   
    #    for item in res:
    #        print item
               
    #    with open("/home/work/KTV-tsyytj.csv","a+") as csvfile: 
    #        writer = csv.writer(csvfile)
    #        writer.writerows(res)
            
    # 热歌经典:
    #def on_start(self):
        #for page in range(1, 111):
            #self.crawl('http://www.boosoochina.com/product/product.php?lang=cn&class3=295&page=%s' % page, callback=self.index_page)
        #for page in range(1, 36):
            #self.crawl('http://www.boosoochina.com/product/product.php?lang=cn&class3=296&page=%s' % page, callback=self.index_page)
            
    #def index_page(self, response):
        
        #res = []
        
        #for each in response.doc('#product-list > ul > li'):
            #name =  each.xpath('span[2]/a')[0].text.strip()
            #artist = each.xpath('span[3]/text()')[0].strip()
            
            #print name
            #print artist
            
            #res.append([artist, name])
            
        #with open("/home/work/KTV-rgjd","a+") as csvfile: 
            #writer = csv.writer(csvfile)
            #writer.writerows(res)
            
    # 新歌展示:
    def on_start(self):
        self.crawl('http://www.boosoochina.com/tsyytj/', callback=self.index_page)

    def index_page(self, response):
        for each in response.doc('dd.sub > h4> a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    def detail_page(self, response):
        fin_href = response.doc('body > div.sidebar.inner > div.sb_box.sbbo > div.active.bsnr > div.web_bottom > div > a:last-child').attr.href
        if fin_href:
            page_sum = int(fin_href.split('=')[-1])
            print page_sum
        
            for page in range(1, page_sum+1):
                url = fin_href.replace('page=%s'%page_sum, 'page=%s'%page)
                print url
                self.crawl(url, callback=self.fetch_data)
    
    def fetch_data(self, response):
        res = []
        
        for each in response.doc('#product-list > ul > li'):
            name =  each.xpath('span[2]/a')[0].text.strip()
            artist = each.xpath('span[3]/text()')[0].strip()
            print name
            print artist
            res.append([artist, name])
            
        with open("/home/work/KTV-xgzs.csv","a+") as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerows(res)

            