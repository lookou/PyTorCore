#!/usr/bin/env python3
import tornado.web
import logging
import json
import re


class PingHandler(tornado.web.RequestHandler):
    async def get(self):
        logging.debug("===== GET Request =====")
        logging.debug(self.request.arguments)
        ret = {"code": 0}
        result = {}
        #args = self.get_argument("args").strip()
        #if  args == "" or pan == "":
        #    ret["code"] = 500
        #    self.write(json.dumps(ret))
        #    return

        result["msg"] = "pong"
        ret["data"] = result
        self.write(json.dumps(ret))
        return

    async def post(self):
        logging.debug("====== Post Request =======")
        ret = {"code": 0}
        #data = json.loads(self.request.body)
        #args = data["args"].strip()
        #if  args == "": 
        #    ret["code"] = 500
        #    self.write(json.dumps(ret))
        #    return

        result = {}
        result["msg"] = "pong"
        ret["data"] = result
        self.write(json.dumps(ret))
        return


