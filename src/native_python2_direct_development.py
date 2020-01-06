#!/usr/bin/
# coding:utf-8

import json
import os
import logging
from threading import Timer


class NativePython2DirectDevelopment(object):
    TAG = "NativePython2DirectDevelopment"

    def __init__(self, tag=None):
        tag = "%s.%s" % (tag, NativePython2DirectDevelopment.TAG)
        self.log = logging.getLogger(tag)
        self.log.info("five_minutes_process__init__")

    def read_json_file(self, json_file_path):
        try:
            if not os.path.exists(json_file_path):
                return {}
            with open(json_file_path, 'r') as f:
                config = f.read()
            return json.loads(config)
        except Exception as e:
            self.log.error("Read %s file is failed: %s" % (json_file_path, str(e)))

    def write_json_file(self, json_file_path, dict):
        try:
            with open(json_file_path, "w") as f:
                json.dump(dict, f)
        except Exception as e:
            self.log.error("Write %s file is failed: %s" % (json_file_path, str(e)))

    def make_sure_path_exists(self, file_path):
        if not os.path.exists(file_path):
            try:
                os.mkdir(file_path, 0777)
                os.chmod(file_path, 0777)
            except Exception as e:
                self.log.error("There is a problem with the %s, msg: %s" % (file_path, str(e)))

    def data_process(self):
        json_file_path = "./temporary_json"
        self.make_sure_path_exists(json_file_path)
        Timer(300, self.data_process, ()).start()