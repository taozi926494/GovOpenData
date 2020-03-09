from typing import List
from GovOpendata.apps.model.Dataset import Dataset
from GovOpendata.apps.model.Government import Government
from ...apps import app, db
import os
from flask import abort


class DatasetSrv(object):
    @classmethod
    def add(cls, name: str, abstract: str, gov_id: int, department: str,
            subject: str, industry: str, extra_info: str, field_info: str,
            view_num: int, download_num: int, collect_num: int, update_date: str,
            acquire_date: str):
        try:
            obj = Dataset(
                name=name,
                abstract=abstract,
                gov_id=gov_id,
                department=department,
                subject=subject,
                industry=industry,
                extra_info=extra_info,
                field_info=field_info,
                view_num=view_num,
                download_num=download_num,
                collect_num=collect_num,
                update_date=update_date,
                acquire_date=acquire_date
            )
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(500, str(e))

    @classmethod
    def query_by_id(cls, _id: int) -> dict:
        obj = Dataset.query.filter_by(id=_id).first()
        if obj:
            return obj.to_dict()
        else:
            abort(400, 'No Result')
