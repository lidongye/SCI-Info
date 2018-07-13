#!/usr/bin/env python
# -*- coding=utf-8 -*-
# author: Dongye Li<dongye@gooalgene.com>
# 2018-07-06 20:04

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from . import models, views