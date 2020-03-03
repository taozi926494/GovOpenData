#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : DatasetSearchSrv.py
# @Time    : 2020-3-2 13:51
# @Software: PyCharm
# @Author  : Taoz
# @contact : xie-hong-tao@qq.com
from GovOpendata.apps.model.dataset import Dataset
from sqlalchemy import and_


class DatasetSearchSrv(object):
    @classmethod
    def search(cls, keyword: str, gov_id=None, dep_id=None, cate_id=None, page=1, num=10, update_order: str = 'desc')\
            -> object:
        """
        搜索数据集
        :param keyword: 关键字
        :param gov_id: 政府平台id
        :param dep_id: 政府部门id
        :param cate_id: 主题分类id
        :param page: 分页页码
        :param num: 每页显示数量
        :param update_order: 更新时间排序
        :return: object
        """
        exp_list = []
        if keyword is not None:
            exp_list.append(Dataset.path.like('%{}%'.format(keyword)))
        if gov_id is not None:
            exp_list.append(Dataset.gov_id == gov_id)
        if dep_id is not None:
            exp_list.append(Dataset.source == dep_id)
        if cate_id is not None:
            exp_list.append(Dataset.subject == dep_id)

        order_exp = None
        if update_order == 'desc':
            order_exp = Dataset.update_date.desc()
        elif update_order == 'asc':
            order_exp = Dataset.update_date

        if len(exp_list) > 0:
            filter_exp = and_(*exp_list)
            pagination = Dataset.query.filter(filter_exp).order_by(order_exp).paginate(page, num, error_out=False)
        else:
            pagination = Dataset.query.order_by(order_exp).paginate(page, num, error_out=False)

        data = []
        for dataset in pagination.items:
            data.append(dataset.to_dict())
        return {
            'total': pagination.total,
            'pages': pagination.pages,
            'has_prev': pagination.has_prev,
            'has_next': pagination.has_next,
            'data': data
        }
