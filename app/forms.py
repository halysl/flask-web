# -*- coding: utf-8 -*-
# @Date    : 2018-05-23 11:37:56
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : $Id$

'''
MVC里的M，代表数据模型
'''
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

# 登录界面表单
class LoginForm(FlaskForm):
    # openid是表单的一个string域，可以输入文本数据
    openid = StringField('openid', validators=[DataRequired()])
    # remember_me是表单的一个单选框域，可以打钩，默认不打钩
    remember_me = BooleanField('remember_me', default=False)