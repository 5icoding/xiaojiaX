# -*- coding:utf-8 -*-
import subprocess
import tempfile
import time
from flask import Blueprint, request, render_template, redirect, jsonify
from app.models import CourseUnits
from app.extensions import db
import os
import random
import datetime
import time

design = Blueprint('design', __name__,url_prefix='/design')

'''
日期:2024-01-26
作者:陈军
完成状态：未完成
功能描述：课程设计者路由
说明：
'''
@design.route('/',methods=("GET", "POST"))
def index():

    return render_template('design/index.html')

'''
日期:2024-01-26
作者:陈军
完成状态：未完成
功能描述: python语言,目前的课程，并为做其他的语言课程。
说明：
'''
@design.route('/python',methods=("GET", "POST"))
def python_course():
    if request.method == "POST":
        #data = request.get_json()
        data = request.get_json()
        print(data['levelId'])
        print(data['exerciseCode'])

        createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        new_course_unit = CourseUnits(
            levelId=data['levelId'],
            courseId=data['courseId'],
            sequence=data['sequence'],
            title=data['title'],
            target=data['target'],
            content=data['content'],
            codeExample=data['codeExample'],
            exercise=data['exercise'],
            exerciseCode=data['exerciseCode'],
            createTime = createTime,
            description=data['description']
        )

        db.session.add(new_course_unit)
        db.session.commit()

        return jsonify({'result': 1, 'b': 2})
    return render_template('design/python.html')


'''
日期:2024-01-26
作者:陈军
完成状态：未完成
功能描述：课程的整体pert的显示
说明：
'''
@design.route('/pert')
def read_pert():
    return render_template('pert/pert.html')

@design.route('/swimbands')
def read_swimBands():
    return render_template('design/swimBands.html')

@design.route('/regroupingtreeview')
def read_regroupingTreeView():
    return render_template('design/regroupingTreeView.html')


@design.route('/addtopalette')
def addToPalette():
    return render_template('design/addToPalette.html')