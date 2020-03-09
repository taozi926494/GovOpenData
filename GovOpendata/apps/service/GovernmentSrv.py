from flask import abort
from GovOpendata.apps.model.Government import Government
from ...apps import db
from sqlalchemy import func


class GovernmentSrv(object):
    @classmethod
    def statistics(cls) -> object:
        all_government = db.session.query(Government).all()
        dataset_num = 0
        file_num = 0
        file_size = 0
        gov_dict = {}
        for government in all_government:
            dataset_num += government.dataset_num
            file_num += file_num
            file_size += file_size
            if gov_dict.get(government.province) is None:
                gov_dict[government.province] = []
            else:
                gov_dict[government.province].append(government.dir_path)

        data = dict()
        data['dataset_num'] = dataset_num
        data['file_num'] = file_num
        data['file_size'] = file_size
        data['gov_num'] = len(all_government)
        data['province_dict'] = gov_dict
        return data

    @classmethod
    def add(cls, province: str, region: str, dir_path: str, file_num: int,
            file_size: int, dataset_num: int, acquire_date: str):
        try:
            obj = Government(
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
            print(e)
            abort(500, '新增数据出错')
