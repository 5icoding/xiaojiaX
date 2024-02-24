#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, request, render_template, redirect

user = Blueprint('user', __name__)

@user.route('/user_list')       
def user_list():    
    return render_template('user_list.html')

@user.route('/user_info')
def user_info():
    return render_template('user_info.html')    

@user.route('/user_edit')
def user_edit():
    return render_template('user_edit.html')

@user.route('/user_add')    
def user_add(): 
    return render_template('user_add.html')

@user.route('/user_delete')
def user_delete():
    return render_template('user_delete.html')