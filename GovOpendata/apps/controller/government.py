from flask import Blueprint, request
import json
from .. import app
from ...apps.service.government import *
from flask_restful import Resource
governmentBp = Blueprint('government', __name__)


class Gov(Resource):
    def get(self):
        """
        查询
        :return:
        """
        pageIndex = request.args.get('pageIndex', None)
        pageSize = request.args.get('pageSize', None)
        data = dataStatistics(pageIndex=pageIndex, pageSize=pageSize)
        return {'code': 200, 'data': data}
