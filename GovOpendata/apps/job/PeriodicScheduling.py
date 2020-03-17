import os
import json
from ..uitls import timestamp2str
from ..service.GovernmentSrv import GovernmentSrv
from ..service.DatasetSrv import DatasetSrv
from ..service.CrawlDataRecordSrv import CrawlDataRecordSrv
from ...apps import app


class PeriodicScheduling(object):
    @classmethod
    def add_data(cls):
        # 遍历文件的根目录
        dataRootPath = app.config.get('DATA_ROOT_PATH')
        for name in os.listdir(dataRootPath):
            absGovnernmentPath = dataRootPath + '/{}'.format(name)
            # 读取last_crawl.josn 文件信息
            with open(absGovnernmentPath + '/last_crawl.json', 'r', encoding="utf-8") as f:
                data = json.loads(f.read())
            # govUrl = 'http://172.16.13.22:5000/government'
            # 查询数据库里是否存在该条记录, 存在则更新， 否则插入
            if GovernmentSrv.is_exist(dir_path=name):
                # 更新数据
                GovernmentSrv.update(
                    province=data["province"],
                    region=data["region"],
                    dir_path=name,
                    file_num=data["file_num"],
                    file_size=data["total_file_size_mb"],
                    dataset_num=data["dataset_count"],
                    acquire_date=timestamp2str(data["crawl_time"])
                )
            else:
                # 插入数据
                GovernmentSrv.add(
                    province=data["province"],
                    region=data["region"],
                    dir_path=name,
                    file_num=data["file_num"],
                    file_size=data["total_file_size_mb"],
                    dataset_num=data["dataset_count"],
                    acquire_date=timestamp2str(data["crawl_time"])
                )
            # 无论数据是否存在， 都向记录表中添加数据，用于数据增长趋势统计
            CrawlDataRecordSrv.add(
                province=data["province"],
                region=data["region"],
                dir_path=name,
                file_num=data["file_num"],
                file_size=data["total_file_size_mb"],
                dataset_num=data["dataset_count"],
                acquire_date=timestamp2str(data["crawl_time"])
            )
            """向dataset表中写入数据或者添加数据"""
            # 遍历指定开放平台文件夹下数据存储文件夹, 数据集根目录
            datasetRootPath = absGovnernmentPath + '/files'
            for datasetName in os.listdir(datasetRootPath):
                # 数据集的绝对路径
                absdatasetPath = datasetRootPath + "/" + datasetName
                # 读取共有基础信息
                with open(absdatasetPath + '/baseinfo.json', 'r', encoding="utf-8") as f:
                    baseinfo = json.loads(f.read())
                # 读取额外信息
                with open(absdatasetPath + '/extrainfo.json', 'r', encoding="utf-8") as f:
                    extrainfo = f.read()
                # 读取字段信息
                with open(absdatasetPath + '/datafield.json', 'r', encoding="utf-8") as f:
                    datafield = f.read()
                if DatasetSrv.is_exist(datasetName):
                    # 由于数据集内的内容不需要改变，故不需要更新， 更新接口可用于后面的浏览次数，下载次数的更新
                    pass
                else:
                    DatasetSrv.add(
                        name=datasetName,
                        abstract=baseinfo["abstract"],
                        gov_id=GovernmentSrv.get_id(dir_path=name),
                        department=baseinfo["source"],
                        subject=baseinfo["subject"],
                        industry="",
                        extra_info=extrainfo,
                        field_info=datafield,
                        view_num=0,
                        download_num=0,
                        collect_num=0,
                        update_date=baseinfo["update_date"],
                        acquire_date=timestamp2str(data["crawl_time"])
                    )
