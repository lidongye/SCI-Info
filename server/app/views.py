#!/usr/bin/env python
# -*- coding=utf-8 -*-
# author: Dongye Li<dongye@gooalgene.com>
# 2018-07-06 20:07

import sys
import json
from flask import request
from . import utility
from . import app, db
from .models import JournalData
args = sys.argv


@app.route('/', methods=['GET'])
def index():
    return "SCI Impact Factor Search Server"


@app.route('/if', methods=['GET'])
def impact_factor():
    try:
        title = request.args.get('title')
    except:
        title = ''
    try:
        gt = float(request.args.get('gt'))
    except:
        gt = None
    try:
        lt = float(request.args.get('lt'))
    except:
        lt = None
    try:
        page_index = int(request.args.get('page_index'))
    except:
        page_index = 1
    try:
        page_size = int(request.args.get('page_size'))
    except:
        page_size = 10
    try:
        order_by = request.args.get('order_by')
    except:
        order_by = order_by if order_by in JournalData.__dict__ else 'IF'
    try:
        order_type = request.args.get('order_type')
    except:
        order_type = 'asc'

    q = db.session.query(JournalData)
    # 搜索title
    if title is not None:
        q = q.filter(JournalData.title.like("%{}%".format(title)))
    # IF值限制
    if gt is not None:
        q = q.filter(JournalData.IF >= gt)
    if lt is not None:
        q = q.filter(JournalData.IF <= lt)
    # 排序
    if order_by:
        if order_type == "asc":
            q = q.order_by(order_by)
        else:
            q = q.order_by(db.desc(order_by))
    else:
        q = q.order_by(db.desc(order_by))
    # 翻页
    q = q.offset((page_index - 1) * page_size).limit(page_size)
    # 检索
    journals = []
    for journal in q.all():
        journals.append(journal.get_dict())
    # response
    return json.dumps({
        'status' : 200,
        'page_index' : page_index,
        'num' : len(journals),
        'data' : journals
    })
