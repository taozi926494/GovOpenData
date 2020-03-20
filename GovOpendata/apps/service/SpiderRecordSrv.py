from flask import abort
from ..model.SpiderRecord import SpiderRecord
from ...apps import db


class SpiderRecordSrv(object):
    @classmethod
    def add(cls, province: str, region: str, dir_path: str, file_num: int,
            file_size: int, dataset_num: int, acquire_date: str):
        try:
            obj = SpiderRecord(
                province=province,
                region=region,
                dir_path=dir_path,
                file_num=file_num,
                file_size=file_size,
                dataset_num=dataset_num,
                acquire_date=acquire_date
            )
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(500, '新增数据出错')