#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, request, render_template, redirect

account = Blueprint('account', __name__, url_prefix="/account")


@account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('account/login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '123456':
            return redirect('/board')       
        else:       
            return render_template('login.html', msg='用户名或密码错误')
        
@account.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET': 
        return render_template('register.html') 
    else:   
        username = request.form.get('username') 
        password = request.form.get('password') 
        if username == 'admin' and password == 'admin': 
            return redirect('/index')   
        else:   
            return render_template('register.html', msg='用户名或密码错误')             
        
@account.route('/logout')      
def logout():   
    return redirect('/login')



