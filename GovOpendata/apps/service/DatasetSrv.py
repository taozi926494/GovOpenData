from GovOpendata.apps.model.Dataset import Dataset
from GovOpendata.apps.model.Government import Government
from ...apps import app, db
import os
from flask import Response


class DatasetSrv(object):
    @classmethod
    def add(cls, name: str=None, abstract: str=None, gov_id: int=None, department: str=None,
            subject: str=None, industry: str=None, extra_info: str=None, field_info: str=None,
            view_num: int=None, download_num: int=None, collect_num: int=None, update_date: str=None,
            acquire_date: str=None) -> object:
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
            return {"status": "success", "data": "数据插入成功！"}
        except Exception as e:
            db.session.rollback()
            return {"status": "error", "data": e}

    @classmethod
    def getInstanceById(cls, id: int=None) -> object:
        obj = Dataset.query.filter_by(id=id).first()
        return obj.to_dict()

    @classmethod
    def getAttachmentInfo(cls, gov_id: int=None, name: str=None) -> object :
        dataRootPath = app.config.get('DATA_PATH')
        gov = Government.query.filter_by(id=gov_id).first()
        filePath = dataRootPath + '/' + gov.dir_path + "/files/" + name
        result = []
        print(filePath)
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
