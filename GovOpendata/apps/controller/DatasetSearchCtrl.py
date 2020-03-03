#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : DatasetCtrl.py
# @Time    : 2020-3-2 11:45
# @Software: PyCharm
# @Author  : Taoz
# @contact : xie-hong-tao@qq.com
from flask import request, jsonify, abort
from flask_restful import Resource, reqparse
from GovOpendata.apps.service.DatasetSearchSrv import DatasetSearchSrv


class DatasetSearchCtrl(Resource):
    def get(self) -> object:
        parser = reqparse.RequestParser()
        parser.add_argument('page', required=True, type=int)
        parser.add_argument('num', required=True, type=int)
        parser.add_argument('update_order', type=str, default='desc', choices=['desc', 'asc'])
        parser.add_argument('keyword', default=None)
        parser.add_argument('gov_id', default=None)
        parser.add_argument('department', default=None)
        parser.add_argument('subject', default=None)
        parser.add_argument('industry', default=None)
        args = parser.parse_args(strict=True)

        res = DatasetSearchSrv.search(keyword=args.keyword,
                                      gov_id=args.gov_id,
                                      department=args.department,
                                      subject=args.subject,
                                      industry=args.industry,
                                      page=args.page,
                                      num=args.num,
                                      update_order=args.update_order)
        return jsonify(res)


