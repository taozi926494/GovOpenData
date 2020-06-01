from flask import abort

from GovOpendata.apps.service import BaseSrv
from ..model.Government import Government
from ..model.Dataset import Dataset
from ...apps import db


class GovernmentSrv(BaseSrv.inject(Government)):
    @classmethod
    def statistics(cls) -> object:
        all_government = db.session.query(Government).all()
        dataset_num = 0
        file_num = 0
        file_size = 0
        gov_dict = {}
        for government in all_government:
            dataset_num += government.dataset_num
            file_num += government.file_num
            file_size += government.file_size
            if gov_dict.get(government.province) is None:
                gov_dict[government.province] = []
            gov_dict[government.province].append({
                'dir_path': government.dir_path,
                'gov_id': government.id,
                'region': government.region
            })

        data = dict()
        data['dataset_num'] = dataset_num
        data['file_num'] = file_num
        data['file_size'] = file_size
        data['gov_num'] = len(all_government)
        data['province_dict'] = gov_dict
        return data

    # @classmethod
    # def add(cls, province: str, region: str, dir_path: str, file_num: int,
    #         file_size: int, dataset_num: int, acquire_date: str):
    #     try:
    #         obj = Government(
    #             province=province,
    #             region=region,
    #             dir_path=dir_path,
    #             file_num=file_num,
    #             file_size=file_size,
    #             dataset_num=dataset_num,
    #             acquire_date=acquire_date
    #         )
    #         db.session.add(obj)
    #         db.session.commit()
    #     except Exception as e:
    #         db.session.rollback()
    #         abort(500, '新增数据出错')
    #
    # @classmethod
    # def update(cls, province: str, region: str, dir_path: str, file_num: int,
    #         file_size: int, dataset_num: int, acquire_date: str):
    #     try:
    #         Government.query.filter_by(dir_path=dir_path).update(
    #             {
    #                 "province": province,
    #                 "region": region,
    #                 "dir_path": dir_path,
    #                 "file_num": file_num,
    #                 "file_size": file_size,
    #                 "dataset_num": dataset_num,
    #                 "acquire_date": acquire_date
    #             }
    #         )
    #         db.session.commit()
    #     except Exception as e:
    #         db.session.rollback()
    #         abort(500, '更新数据出错')

    @classmethod
    def find_by_dir_path(cls, dir_path: str) -> bool:
        return Government.query.filter_by(dir_path=dir_path).first()

    @classmethod
    def get_id(cls, dir_path: str) -> int:
        obj = Government.query.filter_by(dir_path=dir_path).first()
        return obj.id if obj else 0

    @classmethod
    def get_departments(cls, gov_id):
        data = Dataset.query.filter_by(gov_id=gov_id).group_by(Dataset.department).all()
        return [x.department for x in data]

