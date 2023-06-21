#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tornado.ioloop
import tornado.web
from insts.llog import llogger


from controller.ping import PingHandler
import conf

def make_server():
    app =  tornado.web.Application([
        (r"/ping", PingHandler) 
    ])
    server = tornado.httpserver.HTTPServer(app)
    return server

if __name__ == "__main__":
    server = make_server()
    logger = llogger()
    logger.info("SUCCESS|%s"%("LOADED"))
    logger.info("a","b","c")
    server.listen(conf.port)
    tornado.ioloop.IOLoop.current().start()
