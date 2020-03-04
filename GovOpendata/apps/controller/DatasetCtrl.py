from flask import jsonify
from GovOpendata.apps.service.DatasetSrv import DatasetSrv
from flask_restful import Resource, reqparse


class DatasetCtrl(Resource):
    def get(self)-> object:
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True, type=int)
        args = parser.parse_args(strict=True)
        info = DatasetSrv.getInstanceById(id=args.get("id"))
        attachmentInfoList = DatasetSrv.getAttachmentInfo(info.get("gov_id"), info.get("name"))
        return jsonify({
            'data': {'info': info, 'attachmentInfoList': attachmentInfoList}
        })

    def post(self) -> object:
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, type=str)
        parser.add_argument('abstract', required=True, type=str)
        parser.add_argument('gov_id', required=True, type=int)
        parser.add_argument('department', required=True, type=str)
        parser.add_argument('subject', required=True, type=str)
        parser.add_argument('industry', required=True, type=str)
        parser.add_argument('extra_info', required=True, type=str)
        parser.add_argument('field_info', required=True, type=str)
        parser.add_argument('view_num', required=True, type=int)
        parser.add_argument('download_num', required=True, type=int)
        parser.add_argument('collect_num', required=True, type=int)
        parser.add_argument('update_date', required=True, type=str)
        parser.add_argument('acquire_date', required=True, type=str)
        args = parser.parse_args(strict=True)
        res = DatasetSrv.add(
            name=args.get("name"),
            abstract=args.get("abstract"),
            gov_id=args.get("gov_id"),
            department=args.get("department"),
            subject=args.get("subject"),
            industry=args.get("industry"),
            extra_info=args.get("extra_info"),
            field_info=args.get("field_info"),
            view_num=args.get("view_num"),
            download_num=args.get("download_num"),
            collect_num=args.get("collect_num"),
            update_date=args.get("update_date"),
            acquire_date=args.get("acquire_date")
        )
        return jsonify(res)

