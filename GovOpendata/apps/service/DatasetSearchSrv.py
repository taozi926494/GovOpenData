#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : DatasetSearchSrv.py
# @Time    : 2020-3-2 13:51
# @Software: PyCharm
# @Author  : Taoz
# @contact : xie-hong-tao@qq.com
from GovOpendata.apps.model.Dataset import Dataset
from sqlalchemy import and_


class DatasetSearchSrv(object):
    @classmethod
    def search(cls, page: str, num: str,  keyword: str = None, gov_id=None, department=None, subject=None, industry=None
               , update_order: str = 'desc')-> object:
        """
        搜索数据集
        :param page: 分页页码
        :param num: 每页显示数量
        :param keyword: 关键字
        :param gov_id: 政府平台id
        :param department: 政府部门id
        :param subject: 主题分类
        :param industry: 行业分类
        :param update_order: 更新时间排序
        :return: object
        """
        exp_list = []
        if keyword is not None:
            words = keyword.split(' ')
            for word in words:
                exp_list.append(Dataset.name.like('%{}%'.format(word)))
        if gov_id is not None:
            exp_list.append(Dataset.gov_id == gov_id)
        if department is not None:
            exp_list.append(Dataset.department == department)
        if subject is not None:
            exp_list.append(Dataset.subject == subject)
        if industry is not None:
            exp_list.append(Dataset.industry == industry)

        order_exp = Dataset.update_date.desc() if update_order == 'desc' else Dataset.update_date

        if len(exp_list) > 0:
            filter_exp = and_(*exp_list)
            pagination = Dataset.query.filter(filter_exp).order_by(order_exp).paginate(page, num, error_out=False)
        else:
            pagination = Dataset.query.order_by(order_exp).paginate(page, num, error_out=False)

        return {
            'total': pagination.total,
            'pages': pagination.pages,
            'has_prev': pagination.has_prev,
            'has_next': pagination.has_next,
            'data': [dataset.to_dict() for dataset in pagination.items]
        }
