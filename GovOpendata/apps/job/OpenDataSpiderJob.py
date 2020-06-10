#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : SpiderRecordJob.py
# @Time    : 2020-3-17 10:56
# @Software: PyCharm
# @Author  : Taoz
# @contact : xie-hong-tao@qq.com
import os
from ..uitls import timestamp2str, load_json_file
from ..service.GovernmentSrv import GovernmentSrv
from ..service.SpiderRecordSrv import SpiderRecordSrv
from ...apps import app


class OpenDataSpiderJob(object):
    """ 开放平台爬虫任务，用于遍历爬虫元素及及其任务 """
    @classmethod
    def run(cls):
        # 遍历文件的根目录
        spiders_root_path = app.config.get('DATA_ROOT_PATH')
        for spider_name in os.listdir(spiders_root_path):
            print('Spider Name:  %s' % spider_name)
            spider_record_file = spiders_root_path + '/{}/last_crawl.json'.format(spider_name)
            data = load_json_file(spider_record_file)
            data_to_add = {
                "province": data["province"],
                "region": data["region"],
                "dir_path": spider_name,
                "file_num": data["file_num"],
                "file_size": data["total_file_size_mb"],
                "dataset_num": data["dataset_count"],
                "acquire_date": timestamp2str(data["crawl_time"])
            }

            if GovernmentSrv.find_by_dir_path(spider_name) is not None:
                GovernmentSrv.update(**data_to_add)
            else:
                GovernmentSrv.add(**data_to_add)

            # 向记录表中添加数据，用于数据增长趋势统计
            SpiderRecordSrv.add(**data_to_add)



