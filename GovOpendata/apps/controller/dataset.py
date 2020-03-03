from flask import Blueprint, request
from ...apps.service.dataset import *
from flask_restful import Resource
dataSetBp = Blueprint('dataSet', __name__)

class DatasetDetailController(Resource):
    """
    获取指定文件夹内的文件信息
    """
    def get(self):
        """
        查询
        :return:
        """
        path = request.args.get('path', None)
        id = request.args.get('id', None)
        attachmentInfoList = getAttachmentInfo(path=path)
        info = getDatasetById(id)
        return {'code': 200, 'data': {'info': info, 'attachmentInfoList': attachmentInfoList}}


class FileDownloadController(Resource):
    def get(self, path):
        path = app.config.get('DATA_PATH') + path.replace('$', '/')
        return downloadAttachment(path)


class DatasetViewController(Resource):
    def get(self):
        """
        直接查看所有数据信息
        :return:
        """
        pageIndex = int(request.args.get('pageIndex'))
        pageSize = int(request.args.get('pageSize'))

        data = getDatasetViewList(pageIndex=pageIndex, pageSize=pageSize)
        return {'code': 200, 'data': data}


class DatasetDepartmentController(Resource):
    def get(self):
        """
        搜索关键词获取数据信息
        :return:
        """
        pageIndex = int(request.args.get('pageIndex'))
        pageSize = int(request.args.get('pageSize'))
        keyWord = request.args.get('sourceName')
        data = getDatasetByDepartment(keyWord=keyWord, pageIndex=pageIndex, pageSize=pageSize)
        return {'code': 200, 'data': data}
