# -*- encoding:utf-8 -*-

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# 1. 实例化一个Flask 对象
app = Flask(__name__)

# 2. 实例化一个flask_sqlalchemy对象， 用于操作数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@192.168.8.52:3306/hiMarket"
db = SQLAlchemy(app)