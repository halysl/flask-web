# -*- coding:utf-8 -*-

from flask import render_template, redirect, flash

from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'light'}
    posts = [
        {
            'author': {'nickname': 'light'},
            'body': 'Beautiful is better than ugly.'
        },
        {
            'author': {'nickname': 'light'},
            'body': 'Explicit is better than implicit.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID={openid},remember_me={remember_me}'.format(
            openid=form.openid.data, 
            remember_me=form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])
    
