# -*- coding:utf-8 -*-
from flask import Flask

# 创建一个Flask对象，并修改此对象的config
app = Flask(__name__)

from app import views
