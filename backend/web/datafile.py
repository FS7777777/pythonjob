"""
采集记录文件
"""
import os
import time

class datalog(object):
    def __init__(self):
        pass

    def write(self, content):
        """
        将获取内容写入到当前工作目录。文件名按照时间生成
        """
        with open(os.getcwd()+time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),'wb') as f:
            f.write(content)
    