#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @Time    : 2020-3-4 17:35
# @Software: PyCharm
# @Author  : Taoz
# @contact : xie-hong-tao@qq.com
from flask import jsonify
import time


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


def file_iterator(file_path: str, chunk_size: int =512):
    """ 文件读取迭代器 """
    with open(file_path, 'rb') as target_file:
        while True:
            chunk = target_file.read(chunk_size)
            if chunk:
                yield chunk
            else:
                break


def timestamp2str(timeStamp):
    return time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(timeStamp))

