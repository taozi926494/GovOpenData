import base64
import os
from typing import List

from flask import Response
from ...apps import app, Government
from ..uitls import file_iterator
from ..model.Dataset import Dataset


class DatasetFilesSrv(object):
    @classmethod
    def get_files(cls, gov_id: int, dataset_name: str) -> List:
        data_root_path = app.config.get('DATA_ROOT_PATH')
        gov = Government.query.filter_by(id=gov_id).first()
        dataset_files_dir = '{data_root_path}/{gov_dir_path}/files/{dataset_name}'\
            .format(data_root_path=data_root_path, gov_dir_path=gov.dir_path, dataset_name=dataset_name)

        result = []
        for path, file_folder, filename_list in os.walk(dataset_files_dir):
            _path = path.replace('\\', '/')
            for filename in filename_list:
                if not filename in ['metadata.json', 'fieldinfo.json']:
                    abs_path = _path + '/' + filename
                    fsize = os.path.getsize(abs_path)
                    fsize = round(fsize / (1024 * 1024), 2)

                    result.append({"name": filename,
                                   "size": fsize,
                                   'create_time': os.path.getmtime(abs_path)})

        result.sort(key=lambda x: x['create_time'], reverse=True)
        return result

    @classmethod
    def download_files(cls, dataset_id: int, filename: str):
        """
        实现文件的下载功能
        :return: response
        """
        dataset = Dataset.query.filter_by(id=dataset_id).first()
        gov = Government.query.filter_by(id=dataset.gov_id).first()

        file_path = '{data_root_path}/{gov_dir_path}/files/{dataset_name}/{filename}'\
            .format(data_root_path=app.config.get('DATA_ROOT_PATH'),
                    gov_dir_path=gov.dir_path,
                    dataset_name=dataset.name,
                    filename=filename)

        response = Response(file_iterator(file_path))
        response.headers['Content-Type'] = 'application/octet-stream'
        filename = os.path.basename(file_path).encode("utf-8").decode("latin1")
        response.headers["Content-Disposition"] = 'attachment;filename="{}"'.format(filename)
        return response


