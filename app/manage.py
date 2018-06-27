'''初始化数据库'''
from yang import db
from yang.module import *


if __name__=='__main__':
    db.create_all()

