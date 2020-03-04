from flask import abort
from GovOpendata.apps.model.Government import Government
from ...apps import db
from sqlalchemy import func


class GovernmentSrv(object):
    @classmethod
    def statistics(cls) -> object:
        # 对数据集求和
        dataset_num = db.session.query(func.sum(Government.dataset_num)).scalar()
        # 对文件求和
        file_num = db.session.query(func.sum(Government.file_num)).scalar()
        # 对文件大小求和
        file_size = db.session.query(func.sum(Government.file_size)).scalar()
        # 分组统计
        governments = db.session.query(Government.id, Government.province).group_by(
            Government.dir_path).all()
        data = dict()
        data['dataset_num'] = int(dataset_num)
        data['file_num'] = int(file_num)
        data['file_size'] = int(file_size)
        data['governments'] = governments
        return data

    @classmethod
    def add(cls, province: str=None, region: str=None, dir_path: str=None,
            file_num: int=0, file_size: int=0, dataset_num: int=0,
            acquire_date: str=None) -> object:
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
            abort(500, str(e))
