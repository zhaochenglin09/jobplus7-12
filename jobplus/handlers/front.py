# -*- coding: utf-8 -*
# 主页的路由
from flask import Blueprint, render_template, current_app, flash, redirect, url_for

from flask_login import login_required, login_user, logout_user
from jobplus.models import db, User
from jobplus.forms import RegisterForm, LoginForm

front = Blueprint('front', __name__)
@front.route('/')
def index():
	return render_template('index.html')
@front.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		login_user(user, form.remember_me.data)
		return redirect(url_for('.index'))
	return render_template('login.html',form=form)
@front.route('/register_user', methods=['GET','POST'])
def register_user():
	form = RegisterForm()
	if form.validate_on_submit():		
		form.create_user(10)
		flash('注册成功','success')
		return redirect(url_for('front.login'))
	return render_template('register_user.html',form=form)

@front.route('/register_company', methods=['GET','POST'])
def register_company():
	form = RegisterForm()
	if form.validate_on_submit():
		form.create_user(20)
		flash('注册成功','success')
		return redirect(url_for('front.login'))
	return render_template('register_company.html',form=form)
