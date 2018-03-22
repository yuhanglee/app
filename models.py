#!/usr/bin/env python

# encoding: utf-8

'''

@author: liyuhang

@license: (C) Copyright 2013-2017,beijing SQD.

@contact: liyuhang@cryo-service.com

@software: garner

@file: model.py.py

@time: 2018/3/22 20:38

@desc:
'''

from ext import db

class device_info(db.Model):
    __tablename__ = 'device_info'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, nullable=False)
    device_type = db.Column(db.String(64), nullable=False)
    ver = db.Column(db.String(64), nullable=False)
    create_time = db.Column(db.Integer, nullable=False)

    def __init__(self, device_id = 0, device_type = 'A', ver = '1.0', create_time = 0):
        self.device_id = device_id
        self.device_type = device_type
        self.ver = ver
        self.create_time = create_time


