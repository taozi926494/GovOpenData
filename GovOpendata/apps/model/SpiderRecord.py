#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : CrawlerDataRecord.py
# @Time    : 2020-3-9 9:44
# @Software: PyCharm
# @Author  : Taoz
# @contact : xie-hong-tao@qq.com
from GovOpendata.apps.model import db, Base


class SpiderRecord(Base):
    """爬虫记录表"""
    __tablename__ = 'spider_record'
    province = db.Column(db.String(255), comment="平台所属省")
    region = db.Column(db.String(255), comment="平台所属行政区域， 如贵阳市")
    dir_path = db.Column(db.String(255), comment="该工程的文件目录名")

    file_num = db.Column(db.Integer, comment="文件数量")
    file_size = db.Column(db.Integer, comment="文件总大小")
    dataset_num = db.Column(db.Integer, comment="数据集数量")

    acquire_date = db.Column(db.DateTime, comment="采集时间")
