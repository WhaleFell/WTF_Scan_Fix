# coding=utf-8

import requests
import threading
import re

from flask import request


import os

from loguru import logger
import json

from pathlib import Path

# custom
# from app.api import api
# from config import basedir
# from app.utils import *

ROOTPATH: Path = Path(__file__).resolve().parent


class WhatCms:
    def __init__(self, target, file_path, thread_num=15):
        self.cms = []
        self.is_finish = False
        self.g_index = 0
        self.threads = []
        self.lock = threading.Lock()
        self.thread_num = thread_num
        self.target = WhatCms.normalize_target(target)
        self.info = {}
        self.file_path = file_path
        self.line = self.cms_generator()

    @staticmethod
    def request_url(url):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0"
            }
            r = requests.get(url=url, headers=headers, timeout=2)
            logger.info(f"request url: {url}, status_code: {r.status_code}")
            if r.status_code == 200:
                return r.text
            else:
                return ""
        except Exception as e:
            return ""

    @staticmethod
    def normalize_target(target):
        if target.endswith("/"):
            target = target[:-1]
        if target.startswith("http://") or target.startswith("https://"):
            pass
        else:
            target = "http://" + target
        return target

    def find_powered_by(self):
        """
        根据powered by获取cms
        :return:
        """
        html = WhatCms.request_url(self.target)
        match = re.search("Powered by (.*)", html, re.I)
        if match:
            clear_html_cms = re.sub("<.*?>", "", match.group(1))
            cms_name = clear_html_cms.split(" ")[0]
            self.info["cms_name"] = cms_name
            self.info["path"] = "/"
            self.info["match_pattern"] = "powered by " + cms_name
            self.is_finish = True
            return True
        else:
            return False

    # generator
    def cms_generator(self):
        # with open(Path(ROOTPATH, "cms.json").as_posix(), "r", encoding="utf-8") as file:
        #     jd = json.loads(file.read())
        #     for j in jd:
        #         path = j["url"]
        #         pattern = j["re"]
        #         cms_name = j["name"]
        #         yield f"{path}------{pattern}------{cms_name}"

        with open(Path(ROOTPATH, "cms.txt").as_posix(), "r", encoding="utf-8") as file:
            for line in file.readlines():
                if len(line.strip()) == 0 or line.startswith("#"):
                    continue
                yield line.replace("\n", "")

    def find_cms_with_file(self):
        """
        根据cms.txt检测cms
        :return:
        """
        while True:
            if self.is_finish:
                break

            with self.lock:
                line = next(self.line, None)
                logger.success(f"line: {line}")

            # if self.g_index >= len(self.cms):
            if line is None:
                self.lock.acquire()
                self.is_finish = True
                self.info["cms_name"] = "nothing"
                self.info["path"] = "nothing"
                self.info["match_pattern"] = "nothing"
                self.lock.release()
                break

            self.lock.acquire()
            try:
                eachline = line
            except Exception as e:
                break
            self.lock.release()

            if len(eachline.strip()) == 0 or eachline.startswith("#"):
                continue
            else:
                path, pattern, cms_name = eachline.split("------")
                print(path, pattern, cms_name)

            url = self.target + path
            response_html = WhatCms.request_url(url)

            if pattern.lower() in response_html.lower():
                self.lock.acquire()
                self.is_finish = True
                # self.info["cms_name"] = cms_name[:-1]
                self.info["cms_name"] = cms_name
                self.info["path"] = path
                self.info["match_pattern"] = pattern
                self.lock.release()
                break

    def start_threads(self):
        for i in range(self.thread_num):
            t = threading.Thread(target=self.find_cms_with_file)
            self.threads.append(t)

        for t in self.threads:
            t.start()

        for t in self.threads:
            t.join()

    @logger.catch()
    def run(self):
        info = self.find_powered_by()
        if not info:
            self.start_threads()

    def get_result(self):
        while True:
            if self.is_finish:
                return self.info


# custom
from app.api import api
from config import basedir
from app.utils import *


@api.route("/cms")
def cms():
    target = str(request.args.get("target", ""))
    whatcms = WhatCms(target, os.path.join(basedir, "app/api/cms/cms.txt"))
    whatcms.run()
    return success(data=whatcms.get_result())


if __name__ == "__main__":
    # # http://www.asp.com.cn/
    # whatcms = WhatCms("http://www.asp.com.cn/", "cms.txt")
    # whatcms.run()
    # print(whatcms.get_result())
    whatcms = WhatCms("http://www.asp.com.cn/", "cms.txt")
    lines = whatcms.cms_generator()
    # print(next(line))
    # print(next(line))
    # print(next(line))
    for line in lines:
        print(line)
