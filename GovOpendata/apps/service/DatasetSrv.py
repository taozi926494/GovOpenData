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
    def update(cls, name: str, abstract: str, gov_id: int, department: str,
            subject: str, industry: str, extra_info: str, field_info: str,
            view_num: int, download_num: int, collect_num: int, update_date: str,
            acquire_date: str):
        try:
            Dataset.query.filter_by(name=name).update({
                "name": name,
                "abstract": abstract,
                "gov_id": gov_id,
                "department": department,
                "subject": subject,
                "industry": industry,
                "extra_info": extra_info,
                "field_info": field_info,
                "view_num": view_num,
                "download_num": download_num,
                "collect_num": collect_num,
                "update_date": update_date,
                "acquire_date": acquire_date
            })
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(500, str(e))

    @classmethod
    def getAttachmentInfo(cls, gov_id: int=None, name: str=None) -> object :
        dataRootPath = app.config.get('DATA_PATH')
        gov = Government.query.filter_by(id=gov_id).first()
        filePath = dataRootPath + '/' + gov.dir_path + "/files/" + name
        result = []
        for path, fileFolder, fileNameList in os.walk(filePath):
            # 获取所有的文件
            _path = path.replace('\\', '/')
            for fileName in fileNameList:
                # 拼接成绝对路径
                absFilePath = _path + '/' + fileName
                # 获取文件后缀
                _, fileType = os.path.splitext(absFilePath)
                fileType = fileType.replace('.', '')
                # 获取文件大小
                fsize = os.path.getsize(absFilePath)
                fsize = fsize / float(1024 * 1024)
                fsize = round(fsize, 2)
                relativePath = absFilePath.replace(dataRootPath, '')
                result.append({"name": fileName, "type": fileType, "size": fsize, "path": relativePath})
        return result

    @classmethod
    def query_by_id(cls, _id: int) -> dict:
        obj = Dataset.query.filter_by(id=_id).first()
        if obj:
            return obj.to_dict()
        else:
            abort(400, 'No Result')

    @classmethod
    def is_exist(cls, name: str) -> bool:
        obj = Dataset.query.filter_by(name=name).first()
        return True if obj else False