#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, request, render_template, redirect

site = Blueprint('site', __name__)


@site.route('/index')
def index():
    # with SQLHelper() as helper:
    #     user_list = helper.fetchall('select * from users',[])

    return render_template('sites/index.html')

@site.route('/ide')
def read_ide():
    # with SQLHelper() as helper:
    #     user_list = helper.fetchall('select * from users',[])

    return render_template('sites/ide.html')

@site.route('/board')
def read_board():
    # with SQLHelper() as helper:
    #     user_list = helper.fetchall('select * from users',[])

    return render_template('board.html')



