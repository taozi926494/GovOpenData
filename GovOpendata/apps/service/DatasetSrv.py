from typing import List
from GovOpendata.apps.model.Dataset import Dataset
from GovOpendata.apps.service import BaseSrv
from ...apps import app, db
import os
from flask import abort


class DatasetSrv(BaseSrv):
    orm = Dataset

    @classmethod
    def save(cls, **kwargs):
        exist = cls.orm.query.filter_by(gov_id=kwargs['gov_id'], name=kwargs['name']).first()
        try:
            if exist is not None:
                exist.set(kwargs)
            else:
                one = cls.orm()
                one.set(kwargs)
                db.session.add(one)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            abort(400, str(e))

    # @classmethod
    # def getAttachmentInfo(cls, gov_id: int=None, name: str=None) -> object :
    #     dataRootPath = app.config.get('DATA_PATH')
    #     gov = Government.query.filter_by(id=gov_id).first()
    #     filePath = dataRootPath + '/' + gov.dir_path + "/files/" + name
    #     result = []
    #     for path, fileFolder, fileNameList in os.walk(filePath):
    #         # 获取所有的文件
    #         _path = path.replace('\\', '/')
    #         for fileName in fileNameList:
    #             # 拼接成绝对路径
    #             absFilePath = _path + '/' + fileName
    #             # 获取文件后缀
    #             _, fileType = os.path.splitext(absFilePath)
    #             fileType = fileType.replace('.', '')
    #             # 获取文件大小
    #             fsize = os.path.getsize(absFilePath)
    #             fsize = fsize / float(1024 * 1024)
    #             fsize = round(fsize, 2)
    #             relativePath = absFilePath.replace(dataRootPath, '')
    #             result.append({"name": fileName, "type": fileType, "size": fsize, "path": relativePath})
    #     return result
    #

    #
    # @classmethod
    # def is_exist(cls, name: str) -> bool:
    #     obj = Dataset.query.filter_by(name=name).first()
    #     return True if obj else False
