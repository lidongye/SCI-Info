# /bin/python
# -*- coding=utf-8 -*-
#encoding = utf-8

import json

from datetime import datetime
from flask import abort

def check_json_format(raw_msg):
    """
    用于判断一个字符串是否符合Json格式

    :param raw_msg:
    :return:
    """
    if isinstance(raw_msg, str):  # 首先判断变量是否为字符串
        try:
            json.loads(raw_msg, encoding='utf-8')
        except ValueError:
            return False
        return True
    else:
        return False


def get_request_entity(request):
    if request.method == "POST":
        if request.mimetype == "application/json":
            return request.json
        elif request.mimetype == "text/plain":
            entity_json = request.get_data(as_text=True)
            try:
                return json.loads(entity_json, encoding="utf-8")
            except:
                raise ("No Json Data")
        elif request.mimetype == "multipart/form-data":
            return request.form.to_dict()
        else:
            raise ("No Json Data")
    elif request.method == "GET":
        entity_dict = request.args.to_dict()
        return entity_dict
    else:
        raise("method error")



def space_convert(size_long, _round):
    """
    将数字空间大小转换为更大单位字符串

    :param size_long: 数字大小 B 为单位
    :param _round: 小数位数
    :return: 返回带单位
    """
    size_units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    total_times = len(size_units) - 1
    block = 1024.0

    times = 0

    while size_long >= block:
        size_long = size_long / block
        times += 1
        if times >= total_times:
            break

    if _round is not None:
        size_long = round(size_long, _round)
    return "%s %s" % (size_long, size_units[times])


def transfer_str(str):
    new_str = ""
    special = ['*', '.', '?', '+', '$', '^', '[', ']', '{', '}', '|', '/']
    for c in str:
        if c in special:
            new_str += '\\'
        new_str += c
    return new_str
