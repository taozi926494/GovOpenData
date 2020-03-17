from GovOpendata.apps.service.DatasetFilesSrv import DatasetFilesSrv
from flask_restful import Resource, reqparse


class DatasetFilesCtrl(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('dataset_id', required=True, type=int)
        parser.add_argument('filepath', required=True, type=str)
        args = parser.parse_args(strict=True)

        return DatasetFilesSrv.download_files(args.dataset_id, args.filepath)
