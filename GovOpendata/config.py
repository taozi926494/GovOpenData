import os
# 设置应用的运行模式， 是否开启调试模式
DEBUG = True
DATA_ROOT_PATH = '/mnt/nfs/GovOpenDataCrawlers/'
# 数据库配置
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Clc372493@127.0.0.1:3306/govopendata'
SQLALCHEMY_TRACK_MODIFICATIONS = False

