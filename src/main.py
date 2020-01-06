#!/urs/bin/python2
# -*- coding:utf-8 -*-

import logging
import argparse
import os
import sys
import json
from logging.handlers import RotatingFileHandler
from native_python2_direct_development import NativePython2DirectDevelopment

parser = argparse.ArgumentParser()
parser.add_argument("--version", help="business monitor version", action="store_true")
parser.add_argument("--debug", help="print message with level DEBUG", action="store_true")
parser.add_argument("--info", help="print message with level INFO", action="store_true")
parser.add_argument("--warn", help="print message with level WARN", action="store_true")
parser.add_argument("--error", help="print message with level ERROR", action="store_true")
args = parser.parse_args()

BUILD_DATE = '__BUILD_DATE__'
BUILD_VERSION = '__BUILD_VERSION__'
LOG_TAG = "native_python2_direct_development_data"
log_folder_path = "%s/log/" % (os.getcwd())


def init_log(args):
    log_level = logging.ERROR
    if args.debug:
        log_level = logging.DEBUG
    elif args.info:
        log_level = logging.INFO
    elif args.warn:
        log_level = logging.WARNING
    elif args.error:
        log_level = logging.ERROR
    logMaxBytes = 20 * 1024 * 1024
    logBackupCount = 5
    if not os.path.exists(log_folder_path):
        try:
            os.mkdir(log_folder_path, 0777)
            os.chmod(log_folder_path, 0777)
        except Exception as e:
            print e
            return
    logger = logging.getLogger(LOG_TAG)
    logger.setLevel(log_level)
    rHandler = RotatingFileHandler('%s%s.log' % (log_folder_path, LOG_TAG), maxBytes=logMaxBytes,
                                   backupCount=logBackupCount)
    rHandler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s[%(lineno)d] %(message)s')
    rHandler.setFormatter(formatter)
    logger.addHandler(rHandler)


def init_config(config_file_path):
    if not os.path.exists(config_file_path):
        return {}
    with open(config_file_path, 'r') as f:
        config = f.read()
    return json.loads(config)


if __name__ == "__main__":
    if args.version:
        print "{}: {},{}".format(LOG_TAG, BUILD_VERSION, BUILD_DATE)
        sys.exit(0)
    init_log(args)
    log = logging.getLogger(LOG_TAG)
    log.info("%s start ..." % LOG_TAG)
    try:
        config_file_path = os.path.join(os.getcwd(), "native_python2_direct_development.json")
        conf = init_config(config_file_path)
        if not conf:
            log.error("native_python2_direct_development.json file not find")
            sys.exit(-1)
        time_zone = conf.get("time_zone")
        os.environ['TZ'] = time_zone
        native_python2_direct_development = NativePython2DirectDevelopment(LOG_TAG)
        native_python2_direct_development.data_process()
    except Exception as e:
        log.error("main error: %s" % (str(e)))
        sys.exit(-1)
