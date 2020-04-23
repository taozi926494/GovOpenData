#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : DatasetJob.py
# @Time    : 2020-3-17 10:57
# @Software: PyCharm
# @Author  : Taoz
# @contact : xie-hong-tao@qq.com
import os
import json
from concurrent.futures.thread import ThreadPoolExecutor

import requests
from GovOpendata.apps.model import set_model_by_dict
from ..uitls import timestamp2str, load_json_file
from ...apps import app, db
from flask import abort
from ..model.Dataset import Dataset
from ..model.Government import Government



class DatasetJob(object):
    @classmethod
    def run(cls, dir_path:str):
        # 遍历文件的根目录
        spiders_root_path = app.config.get('DATA_ROOT_PATH')
        executor = ThreadPoolExecutor(max_workers=16)
        if dir_path:
            files_path = spiders_root_path + '/{}/files'.format(dir_path)
            gov = Government.query.filter_by(dir_path=dir_path).first()

            queue = []
            # 遍历指定开放平台文件夹下数据存储文件夹, 数据集根目录
            for dataset_name in os.listdir(files_path):
                # cls.handel_dataset((files_path, dataset_name, gov.id))
                if len(queue) < 16:
                    queue.append((files_path, dataset_name, gov.id))
                else:
                    executor.map(cls.handel_dataset, queue)
                    queue = []
        else:
            for spider_name in os.listdir(spiders_root_path):
                files_path = spiders_root_path + '/{}/files'.format(spider_name)
                gov = Government.query.filter_by(dir_path=spider_name).first()

                queue = []
                # 遍历指定开放平台文件夹下数据存储文件夹, 数据集根目录
                for dataset_name in os.listdir(files_path):
                    # cls.handel_dataset((files_path, dataset_name, gov.id))
                    if len(queue) < 16:
                        queue.append((files_path, dataset_name, gov.id))
                    else:
                        executor.map(cls.handel_dataset, queue)
                        queue = []

    @classmethod
    def handel_dataset(cls, tpl: tuple):
        files_path = tpl[0]
        dataset_name = tpl[1]
        gov_id = tpl[2]

        dataset_path = files_path + "/" + dataset_name
        baseinfo = load_json_file(dataset_path + '/baseinfo.json')
        extrainfo = load_json_file(dataset_path + '/extrainfo.json', parse=False)
        datafield = load_json_file(dataset_path + '/datafield.json', parse=False)

        if baseinfo.get('source') is None:
            return

        print(dataset_name)

        exist = Dataset.query.filter_by(gov_id=gov_id, name=dataset_name).first()
        if exist is not None:
            set_model_by_dict(exist, {
                'update_date': baseinfo['update_date']
            })
        else:
            one = Dataset()
            set_model_by_dict(one, {
                "name": dataset_name,
                "abstract": baseinfo["abstract"],
                "gov_id": gov_id,
                "department": baseinfo["source"],
                "subject_auto": cls.auto_classify(dataset_name),
                "subject_origin": baseinfo["subject"],
                "update_date": baseinfo["update_date"],
                "industry": "",
                "extra_info": extrainfo,
                "field_info": datafield,
            })
            db.session.add(one)
            db.session.commit()

    @classmethod
    def auto_classify(cls, text):
        url = 'http://172.16.119.13/api/govern-classify/catalogue/autocatalogue/catalogue'
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "token": "dd3e108b2b369a75cb57cb59087bf4d5"
        }
        body = {
            "text": text
        }
        res = requests.post(url, headers=headers, json=body)
        result = json.loads(res.text)
        if result["code"] == 10000:
            return result['result'][0]
