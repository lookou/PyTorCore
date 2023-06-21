#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import MySQLdb
import mysql.connector
import tornado.ioloop
import tornado.web
import json
from insts.llog import llogger
from insts.basic import * 

@singleton
class DBMgr:
    db = None
    def __init__(self, host, user, passwd, dbname):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.logger = llogger()


        if self.db == None:
            self.logger.info(self.host, self.user, self.passwd, self.dbname)
            self.db = mysql.connector.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.dbname, auth_plugin='mysql_native_password')
            self.__cursor__ = self.db.cursor()

    def inner_check_conn(self):
        try:
            self.db.ping()
        except:
            self.db = mysql.connector.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.dbname, auth_plugin='mysql_native_password')
            self.__cursor__ = self.db.cursor()

    def query_one(self, query):
        # 使用execute方法执行SQL语句
        self.inner_check_conn()

        self.logger.debug(query)
        self.__cursor__.execute(query)
        # 使用 fetchone() 方法获取一条数据
        data = self.__cursor__.fetchone()
        return data
    def query_many(self, query):
        # 使用execute方法执行SQL语句
        self.inner_check_conn()
        self.logger.debug(query)
        self.__cursor__.execute(query)
        # 使用 fetchone() 方法获取多条数据
        data = self.__cursor__.fetchall()
        return data
    def cursor(self):
        return self.db.cursor()

    def commit(self):
        self.logger.debug("Database commit")
        self.db.commit()

    def __del__(self):
        # 关闭数据库连接
        if self.db != None:
            self.db.close()




class MySQLMgr:
    db = None
    def __init__(self, host, user, passwd, dbname):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.logger = llogger()


        if self.db == None:
            self.logger.info(self.host, self.user, self.passwd, self.dbname)
            self.db = mysql.connector.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.dbname, auth_plugin='mysql_native_password')
            self.__cursor__ = self.db.cursor()

    def inner_check_conn(self):
        try:
            self.db.ping()
        except:
            self.db = mysql.connector.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.dbname, auth_plugin='mysql_native_password')
            self.__cursor__ = self.db.cursor()

    def query_one(self, query):
        # 使用execute方法执行SQL语句
        self.inner_check_conn()

        self.logger.debug(query)
        self.__cursor__.execute(query)
        # 使用 fetchone() 方法获取一条数据
        data = self.__cursor__.fetchone()
        return data
    def query_many(self, query):
        # 使用execute方法执行SQL语句
        self.inner_check_conn()
        self.logger.debug(query)
        self.__cursor__.execute(query)
        # 使用 fetchone() 方法获取多条数据
        data = self.__cursor__.fetchall()
        return data

    def cursor(self):
        return self.db.cursor()

    def commit(self):
        self.logger.debug("Database commit")
        self.db.commit()

    def __del__(self):
        # 关闭数据库连接
        if self.db != None:
            self.db.close()

