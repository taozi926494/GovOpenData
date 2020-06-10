#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : NewsCtrl.py
# @Time    : 2020-3-20 10:25
# @Software: PyCharm
# @Author  : Taoz
# @contact : xie-hong-tao@qq.com
from flask_restful import Resource, reqparse
from GovOpendata.apps.service.NewsSrv import NewsSrv
from ..uitls import success_res


class NewsCtrl(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, required=True)
        args = parser.parse_args()

        return success_res(NewsSrv.news_list(page=args.page))

