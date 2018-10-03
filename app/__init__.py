# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 创建一个Flask对象，并修改此对象的config
app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy()
db.init_app(app)

from app import views, models
