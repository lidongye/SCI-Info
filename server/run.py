#!/usr/bin/env python
# -*- coding=utf-8 -*-
# author: Dongye Li<dongye@gooalgene.com>
# 2018-07-06 20:03

import sys
from app import app
args = sys.argv


def main(args):
    app.run('127.0.0.1', 8880)


if __name__ == '__main__':
    main(args)