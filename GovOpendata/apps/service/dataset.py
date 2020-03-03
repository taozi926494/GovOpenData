from ..model.dataset import Dataset
from ...apps import app, db
import os
from flask import Response
import json


def getDatasetQueryList(gov_id=None, pageIndex=1, pageSize=10):
    """
    # 获取query对应的数据结果
    :param gov_id:
    :param pageIndex:
    :param pageSize:
    :return:
    """
    result = dict()
    data_info = list()
    # 获取搜索结果总数
    nums = db.session.query(db.func.count(Dataset.gov_id)).filter(Dataset.gov_id == gov_id).scalar()
    # 根据pageIndex、pageSize参数分页显示数据结果，查询-》筛选—》排序-》分页显示
    data_page_info = db.session.query(Dataset). \
        filter(Dataset.gov_id == gov_id). \
        order_by(Dataset.date_created.desc()). \
        paginate(pageIndex, pageSize, False).items

    for data in data_page_info:
        data_info.append(obj2dict(data))

    # 将输出结果返回
    result['nums'] = str(nums)
    result['data_page_info'] = data_info
    return result


def getDatasetSearchList(keyWord=None, pageIndex=None, pageSize=None):
    """
    获取search对应的数据结果
    :param gov_id:
    :param pageIndex:
    :param pageSize:
    :return:
    """

    result = dict()
    data_info = list()

    # 获取搜索结果总数
    nums = db.session.query(Dataset).filter(Dataset.path.like("%" + keyWord + "%")).count()

    data_page_info = db.session.query(Dataset). \
        filter(Dataset.path.like("%" + keyWord + "%")). \
        order_by(Dataset.date_created.desc()). \
        paginate(pageIndex, pageSize, False).items

    for data in data_page_info:
        data_info.append(obj2dict(data))

    # 将输出结果返回
    result['nums'] = str(nums)
    result['data_page_info'] = data_info

    return result


def obj2dict(obj):
    """
    列表信息转字典
    :param obj:
    :return:
    """
    dic = {}
    for column in obj.__table__.columns:
        dic[column.name] = str(getattr(obj, column.name))
    return dic


def getAttachmentInfo(path=None):
    dataRootPath = app.config.get('DATA_PATH')
    filePath = dataRootPath + '/' + path
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
            relativePath = absFilePath.replace(dataRootPath, '').replace('/', '$')
            result.append({"name": fileName, "type": fileType, "size": fsize, "path": relativePath})
    return result


def getDatasetById(id=None):
    obj = Dataset.query.filter_by(id=id).first()
    return obj2dict(obj)


def downloadAttachment(path=None):
    """
    实现文件的下载功能
    :return: response
    """
    def file_iterator(file_path, chunk_size=512):
        """
            文件读取迭代器
        :param file_path:文件路径
        :param chunk_size: 每次读取流大小
        :return:
        """
        with open(file_path, 'rb') as target_file:
            while True:
                chunk = target_file.read(chunk_size)
                if chunk:
                    yield chunk
                else:
                    break
    dataRootPath = path
    filename = os.path.basename(dataRootPath).encode("utf-8").decode("latin1")
    response = Response(file_iterator(dataRootPath))
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers["Content-Disposition"] = 'attachment;filename="{}"'.format(filename)
    return response


def getDatasetViewList(pageIndex=None, pageSize=None):
    '''
    直接获取数据集列表
    :param keyWord:
    :param pageIndex:
    :param pageSize:
    :return:
    '''

    result = dict()
    data_info = list()

    # 直接获取数据总数

    nums = db.session.query(db.func.count(Dataset.id)).scalar()

    data_page_info = db.session.query(Dataset). \
        order_by(Dataset.date_created.desc()). \
        paginate(pageIndex, pageSize, False).items

    for data in data_page_info:
        data_info.append(obj2dict(data))

    # 将输出结果返回
    result['nums'] = str(nums)
    result['data_page_info'] = data_info

    return result


def getDatasetByDepartment(keyWord=None, pageIndex=None, pageSize=None):
    """
     # 获取search对应的数据结果
     :param gov_id:
     :param pageIndex:
     :param pageSize:
     :return:
    """
    result = dict()
    data_info = list()
    # 获取搜索结果总数
    nums = db.session.query(Dataset).filter(Dataset.source.like("%" + keyWord + "%")).count()
    data_page_info = db.session.query(Dataset). \
        filter(Dataset.source.like("%" + keyWord + "%")). \
        order_by(Dataset.date_created.desc()). \
        paginate(pageIndex, pageSize, False).items
    for data in data_page_info:
        data_info.append(obj2dict(data))
    # 将输出结果返回
    result['nums'] = str(nums)
    result['data_page_info'] = data_info
    return result