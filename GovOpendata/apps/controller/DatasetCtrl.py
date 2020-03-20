from GovOpendata.apps.service.DatasetSrv import DatasetSrv
from GovOpendata.apps.uitls import success_res, error_res
from ..service.DatasetFilesSrv import DatasetFilesSrv
from flask_restful import Resource, reqparse


class DatasetCtrl(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True, type=int)
        args = parser.parse_args(strict=True)

        dataset = DatasetSrv.query_by_id(_id=args.id)
        dataset['files'] = DatasetFilesSrv.get_files(dataset["gov_id"], dataset["name"])

        return success_res(dataset)

    def post(self):
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
        DatasetSrv.save(
            name=args.name,
            abstract=args.abstract,
            gov_id=args.gov_id,
            department=args.department,
            subject=args.subject,
            industry=args.industry,
            extra_info=args.extra_info,
            field_info=args.field_info,
            view_num=args.view_num,
            download_num=args.download_num,
            collect_num=args.collect_num,
            update_date=args.update_date,
            acquire_date=args.acquire_date
        )
        return success_res()

    def put(self) -> object:
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
        DatasetSrv.save(
            name=args.name,
            abstract=args.abstract,
            gov_id=args.gov_id,
            department=args.department,
            subject=args.subject,
            industry=args.industry,
            extra_info=args.extra_info,
            field_info=args.field_info,
            view_num=args.view_num,
            download_num=args.download_num,
            collect_num=args.collect_num,
            update_date=args.update_date,
            acquire_date=args.acquire_date
        )
        return success_res()
