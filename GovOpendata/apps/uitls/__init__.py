#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @Time    : 2020-3-4 17:35
# @Software: PyCharm
# @Author  : Taoz
# @contact : xie-hong-tao@qq.com
from flask import jsonify


def success_res(data=None) -> dict:
    return jsonify({
        'status': 'ok',
        'data': data
    })


def error_res(msg: str) -> dict:
    return jsonify({
        'status': 'error',
        'message': msg
    })

