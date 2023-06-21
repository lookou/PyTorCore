import logging
import os
from inspect import currentframe, getframeinfo
from insts.basic import * 
import conf

@singleton
class llogger:
    def __init__(self):
        LOG_FORMAT = "%(asctime)s|%(levelname)s|%(message)s"
        logname = {}
        logname["INFO"] = logging.INFO
        logname["DEBUG"] = logging.DEBUG
        logname["NOTSET"] = logging.NOTSET
        if conf.logout == "file":
            logging.basicConfig(filename='local.log', level=logname[conf.loglevel], format=LOG_FORMAT)
        else:
            logging.basicConfig(level=logname[conf.loglevel], format=LOG_FORMAT)
            

    def join_with_separator(self, *args, separator='|'):
        return separator.join(str(arg) for arg in args)

    def info(self, *args):
        if len(args) > 0:
            frameinfo = getframeinfo(currentframe().f_back)
            logging.info("%s:%d|%s",os.path.basename(frameinfo.filename), frameinfo.lineno, self.join_with_separator(*args))

    def error(self, *args):
        if len(args) > 0:
            frameinfo = getframeinfo(currentframe().f_back)
            logging.error("%s:%d|%s",os.path.basename(frameinfo.filename), frameinfo.lineno, self.join_with_separator(*args))

    def warn(self, *args):
        if len(args) > 0:
            frameinfo = getframeinfo(currentframe().f_back)
            logging.warn("%s:%d|%s",os.path.basename(frameinfo.filename), frameinfo.lineno, self.join_with_separator(*args))

    def debug(self, *args):
        if len(args) > 0:
            frameinfo = getframeinfo(currentframe().f_back)
            logging.debug("%s:%d|%s",os.path.basename(frameinfo.filename), frameinfo.lineno, self.join_with_separator(*args))


    def trace(self, *args):
        if len(args) > 0:
            frameinfo = getframeinfo(currentframe().f_back)
            logging.trace("%s:%d|%s",os.path.basename(frameinfo.filename), frameinfo.lineno, self.join_with_separator(*args))

