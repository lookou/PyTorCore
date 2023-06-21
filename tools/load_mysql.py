#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import logging
import json
from llog import llogger
from mongo_mgr import MongoMgr
from db_mgr import DBMgr
from bson.objectid import ObjectId
import conf
import time
import copy

db_mgr = DBMgr(conf.host, conf.user, conf.passwd, conf.dbname)
logger = llogger()

if __name__ == "__main__":
    print("Load Black User")
    #data = db_mgr.query_many("select user, channels from blacklist where total >= 3 LIMIT 100;");
    data = db_mgr.query_many("select * from database.tablename where a = 1;");
    for row in data:
        #print(row[0], row[1])
        channels = json.loads(row[1])
        isBlack = False
        for k,v in channels.items():
            #print(k, v)
            if (v >= 3):
                isBlack = True
        if isBlack == True:
            print(row[0],"\t", row[1])



