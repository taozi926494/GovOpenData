#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : DatasetCtrl.py
# @Time    : 2020-3-2 11:45
# @Software: PyCharm
# @Author  : Taoz
# @contact : xie-hong-tao@qq.com
from flask import request, jsonify, abort
from flask_restful import Resource, reqparse
from GovOpendata.apps.utils import ERRORS
from GovOpendata.apps.service.DatasetSearchSrv import DatasetSearchSrv


class DatasetSearchCtrl(Resource):
    def get(self) -> object:
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', required=True)
        parser.add_argument('page', required=True, type=int)
        parser.add_argument('num', required=True, type=int)
        parser.add_argument('update_order', type=str, default='desc', choices=['desc', 'asc'])
        parser.add_argument('gov_id', default=None)
        parser.add_argument('dep_id', default=None)
        parser.add_argument('cate_id', default=None)
        args = parser.parse_args(strict=True)

        res = DatasetSearchSrv.search(args.keyword,
                                      args.gov_id,
                                      args.dep_id,
                                      args.cate_id,
                                      args.page,
                                      args.num,
                                      args.update_order)
        return jsonify(res)


