#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# pyspider结果保存到数据库简单样例,用peewee代替MySQLdb实现数据库操作.
from peewee import *

mysql_db = MySQLDatabase(
    host='',
    port=3306,
    database='kugou',
    user="root",
    passwd="",
    charset='utf8'
)


class BaseModel(Model):
    class Meta:
        database = mysql_db


class testModel(BaseModel):
    name = CharField(null=True, default='')
    artist = CharField(null=True, default='')

    class Meta:
        db_table = 'peewee_test'


class ToMysql():

    def __init__(self):
        tables = [testModel]
        mysql_db.create_tables(tables, safe=True)

    def insert_into_test(self, **data):
        model = testModel()
        for k, v in data.iteritems():
            print k, v
            setattr(model, k, v)
        model.save()
