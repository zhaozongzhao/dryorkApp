#encoding = utf-8
import logging
import logging.config
import time

#从指定的fname的配置文件中读取logging配置文件，文件格式参见
logging.config.fileConfig("logger1.conf", defaults=None, disable_existing_loggers=True)

def debug(message):
     #打印debug级别的日志
     logging.debug(message)

def warning(message):
     #打印warning级别的日志
     logging.warning(message)

def info(message):
     #打印info级别的日志
     logging.info(message)
