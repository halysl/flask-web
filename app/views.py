'''
MVC的V，代表视图，负责界面的渲染
'''

from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# 通过装饰器app.route，将render对象连接到url
@app.route('/')
@app.route('/index')
# 主页视图
def index():
    # 设置的一些数据，之后将作为render_template()的参数使用
    user = {'nickname':'Light'}
    posts = [
        {
            'author':{'nickname':'YAGAMI'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author':{'nickname':'Light'},
            'body':'The avengers movie was so cool!'
        }
    ]
    # render_template()方法，第一个参数制定html文件，之后的参数将通过jinja2模板传递到html文件中
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

# 登录视图
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    # 对表单的验证
    if form.validate_on_submit():
        # flash方法，方便调试，可以将表单数据展示出来
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        # redirect()方法，重定向
        return redirect('/index')
    #注意这个渲染方法的providers的数据来源自app的配置文件
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])