#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import unicode_literals

from flask import (Flask, render_template, redirect, url_for, request, flash)
from flask_bootstrap import Bootstrap
from ext import db
from models import device_info

app = Flask(__name__)
bootstrap = Bootstrap(app)

SECRET_KEY = 'This is my key'

app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:liyuhang@127.0.0.1/app"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db.init_app(app)

@app.route('/')
def index():
    devices = device_info.query.all()
    return render_template('index.html', devices = devices)

@app.route('/device/<string:id>')
def device(id):
    return render_template('device.html', id = id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
