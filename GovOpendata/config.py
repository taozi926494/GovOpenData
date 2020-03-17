import os
# 设置应用的运行模式， 是否开启调试模式
DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# 数据库配置
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/govopendata'
SQLALCHEMY_TRACK_MODIFICATIONS = False

DATA_ROOT_PATH = r"D:/Code/Python/crawlers/opendata政府开放平台"