#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : JobCtrl.py
# @Time    : 2020-3-17 16:18
# @Software: PyCharm
# @Author  : Taoz
# @contact : xie-hong-tao@qq.com
from flask_restful import Resource, reqparse
from ..uitls import success_res
from ..job.OpenDataSpiderJob import OpenDataSpiderJob
from ..job.DatasetJob import DatasetJob
from flask import abort


class JobCtrl(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('type', default=None, type=str, choices=['spider', 'dataset'])
        parser.add_argument('dir_path', default=None, type=str)
        parser.add_argument('token', type=str)
        args = parser.parse_args()

        if args.token != 'CeTcBiGData':
            abort(400)

        if args.type == 'spider':
            OpenDataSpiderJob.run()
            return success_res()
        else:
            DatasetJob.run(args.dir_path)
            return success_res()


