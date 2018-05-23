# 初始化

from flask import Flask

# 创建一个Flask对象，并修改此对象的config
app = Flask(__name__)
app.config.from_object('config')

# 从app对象导入视图方法
from app import views