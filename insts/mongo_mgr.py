#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pymongo
from pymongo.errors import ConnectionFailure
import json
from insts.llog import llogger
from insts.basic import *


@singleton
class MongoMgr:
    mongodb = None
    def __init__(self, mongo_url, mongo_dbname):
        self.mongo_url = mongo_url
        self.mongo_dbname = mongo_dbname
        self.logger = llogger()

        if self.mongodb == None:
            self.logger.info(self.mongo_url)
            self.mongo_cli = pymongo.MongoClient(self.mongo_url)
            self.mongodb = self.mongo_cli[self.mongo_dbname]

    def inner_check_conn(self):
        try:
            pymongo.MongoClient().admin.command('ping')
        except ConnectionFailure:
            self.mongo_cli = pymongo.MongoClient(self.mongo_url)
            self.mongodb = self.mongo_cli[self.mongo_dbname]

    def find_one(self, col_name, query):
        # 使用execute方法执行SQL语句
        self.inner_check_conn()

        self.logger.debug("find_one|%s|%s"%(col_name, query))
        local_col = self.cursor(col_name)
        one = local_col.find_one(query)
        #self.logger.debug("ret: %s"%(one))
        return one

    def find_many(self, col_name, query):
        # 使用execute方法执行SQL语句
        self.inner_check_conn()

        self.logger.debug("find|%s|%s"%(col_name, query))
        local_col = self.cursor(col_name)
        many = local_col.find(query)
        #self.logger.debug("ret: %s"%(many))
        return many

    def insert_one(self, col_name, query):
        # 使用execute方法执行SQL语句
        self.inner_check_conn()

        self.logger.info("insert|%s|%s"%(col_name, query))
        local_col = self.cursor(col_name)
        ret = local_col.insert_one(query)
        #self.logger.debug("ret: %s"%(ret))
        return ret

    def update_one(self, col_name, query, value):
        # 使用execute方法执行SQL语句
        self.inner_check_conn()

        self.logger.info("update|%s|%s|%s"%(col_name, query,value))
        local_col = self.cursor(col_name)
        newvalues = { "$set": value }
        ret = local_col.update_one(query, newvalues)
        #self.logger.debug("ret: %s"%(ret))
        return ret

    def delete_one(self, col_name, query):
        # 使用execute方法执行SQL语句
        self.inner_check_conn()

        self.logger.info("delete|%s|%s"%(col_name, query))
        local_col = self.cursor(col_name)
        ret = local_col.delete_one(query)
        #self.logger.debug("ret: %s"%(ret))
        return ret

    def cursor(self, col_name):
        return self.mongodb[col_name]


    def __del__(self):
        # 关闭数据库连接
        if self.mongo_cli != None:
            self.mongo_cli.close()


