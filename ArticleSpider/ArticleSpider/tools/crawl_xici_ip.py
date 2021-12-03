# -*- coding: utf-8 -*-
__author__ = 'XY'
from typing_extensions import ParamSpec
import requests
from scrapy.selector import Selector


def crawl_ips():
    pass


class GetIP(object):
    def delete_ip(self, ip):
        pass

    def judge_ip(self, ip, port):
        pass


    def get_random_ip(self):
        pass



# print (crawl_ips())
if __name__ == "__main__":
    get_ip = GetIP()
    get_ip.get_random_ip()