import os
from flask import Response
from ...apps import app


class DatasetFileDownloadSrv(object):

    @classmethod
    def downloadAttachment(cls, path: str=None):
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
        dataRootPath = app.config.get('DATA_PATH') + '/' + path
        filename = os.path.basename(dataRootPath).encode("utf-8").decode("latin1")
        response = Response(file_iterator(dataRootPath))
        response.headers['Content-Type'] = 'application/octet-stream'
        response.headers["Content-Disposition"] = 'attachment;filename="{}"'.format(filename)
        return response

