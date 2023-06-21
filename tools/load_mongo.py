#!/usr/bin/env python3

import logging
import json
from llog import llogger
from mongo_mgr import MongoMgr
from bson.objectid import ObjectId
import conf
import time
import copy

mongo_mgr = MongoMgr(conf.mongo_url, conf.mongo_dbname)
logger = llogger()

if __name__ == "__main__":
    print("Load File")
    now = int(time.time())
    expire = now - 86400
    #expire = now - 10
    query = { "$where" : "this.nodes.length > 2"}
    docs = mongo_mgr.find_many("ipaddrs", query)
    for doc in docs:
        #do = json.loads(doc)
        print(doc["nodes"])
        for v in doc["nodes"]:
            print(v["uid"],time.strftime("%Y%m%d %H:%M:%S", time.localtime(v["time"])), v["channel"])



