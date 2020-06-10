from flask import jsonify
from flask_restful import Resource, reqparse
from GovOpendata.apps.service.GovernmentSrv import GovernmentSrv
from GovOpendata.apps.uitls import success_res


class GovernmentCtrl(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('gov_id', default=None, type=int)
        args = parser.parse_args()

        if args.gov_id is not None:
            data = GovernmentSrv.get_departments(gov_id=args.gov_id)
            success_res(data)
        else:
            data = GovernmentSrv.statistics()
        return success_res(data)

    def post(self)->object:
        parser = reqparse.RequestParser()
        parser.add_argument('province', required=True, type=str)
        parser.add_argument('region', required=True, type=str)
        parser.add_argument('dir_path', required=True, type=str)
        parser.add_argument('file_num', required=True, type=int)
        parser.add_argument('file_size', required=True, type=int)
        parser.add_argument('dataset_num', required=True, type=int)
        parser.add_argument('acquire_date', required=True, type=str)
        args = parser.parse_args(strict=True)

        data = GovernmentSrv.save(**args)
        return success_res(data)

    def put(self) -> object:
        parser = reqparse.RequestParser()
        parser.add_argument('province', required=True, type=str)
        parser.add_argument('region', required=True, type=str)
        parser.add_argument('dir_path', required=True, type=str)
        parser.add_argument('file_num', required=True, type=int)
        parser.add_argument('file_size', required=True, type=int)
        parser.add_argument('dataset_num', required=True, type=int)
        parser.add_argument('acquire_date', required=True, type=str)
        args = parser.parse_args(strict=True)
        # TODO 由于没有id 暂时不能用save，若要用save只能添加id参数，并且修改前端参数值
        data = GovernmentSrv.update(
            province=args.get("province"),
            region=args.get("region"),
            dir_path=args.get("dir_path"),
            file_num=args.get("file_num"),
            file_size=args.get("file_size"),
            dataset_num=args.get("dataset_num"),
            acquire_date=args.get("acquire_date")
        )
        return success_res(data)

