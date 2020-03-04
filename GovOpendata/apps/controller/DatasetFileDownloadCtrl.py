from GovOpendata.apps.service.DatasetFileDownloadSrv import DatasetFileDownloadSrv
from flask_restful import Resource, reqparse


class DatasetFileDownloadCtrl(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('path', required=True, type=str)
        args = parser.parse_args(strict=True)
        return DatasetFileDownloadSrv.downloadAttachment(path=args.get("path"))
