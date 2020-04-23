#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : manage.py
# @Time    : 2020-4-23 10:21
# @Software: PyCharm
# @Author  : Taoz
# @contact : xie-hong-tao@qq.com

from GovOpendata.apps import app, db


def create_db():
    db.init_app(app)
    db.create_all()


if __name__ == '__main__':
    create_db()