#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json
import requests
from insts.llog import llogger
from insts.basic import *

@singleton
class NoticeMgr:
    def __init__(self):
        self.logger = llogger()

    def info(self, text):
        url = 'https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxx'
        headers = { 
            "Content-Type": "application/json" 
        }   
        formdata = { 
            "msg_type":"text",
            "content": {"text":str(text)}
        }   
        self.logger.info(formdata)
        requests.post(url=url, data=json.dumps(formdata),headers=headers)

if __name__== "__main__":
    notice_mgr = NoticeMgr()
    notice_mgr.info("a\nb")
