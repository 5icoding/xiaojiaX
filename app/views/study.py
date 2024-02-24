# -*- coding:utf-8 -*-
from flask import Blueprint, request, render_template, redirect, session,jsonify
from app.models import RecordCurrentStudy,CourseUnits
from app.extensions import db
import json

'''
日期:2024-01-26
作者:陈军
完成状态：未完成
功能描述：路由类
说明：
'''
study = Blueprint('study', __name__, url_prefix="/study")

'''
日期:2024-01-26
作者:陈军
完成状态：
功能描述：路由,学生登陆后，首页
说明：
'''
@study.route('/')
def index():
    return render_template('study/index.html',userName = session.get('user_name'))

'''
日期:2024-01-26
作者:陈军
完成状态：
功能描述：api,smallfivestar,网页初始，获取当前课程信息；学生活动，动作信息保存；获得下一刻课程信息；
说明：
'''
@study.route('/getCurrentUnit', methods=['GET', 'POST'])
def get_current_unit():
    if request.method == "POST":

        
        return "POST"
    
    user_id = session.get('user_id')
    print('userId-->' + str(user_id))

    rcs = RecordCurrentStudy.query.filter(RecordCurrentStudy.learnerId == 1).first()
    print(rcs)

    unit = CourseUnits.query.filter(CourseUnits.sequence == rcs.unitId).first()

    print(unit.codeExample)

    result = {'codeExample':unit.codeExample,'target':unit.target,'exercise':unit.exercise,'content':unit.content}
    #user = User.query.filter_by(username='test').first()

    #users = RecordCurrentStudy.query.all()

    #result = {'id':rcs.id,'':rcs.unitId}
    return jsonify({'result':'success','data':result})

'''
日期:2024-01-26
作者:陈军
完成状态：
功能描述：路由,任务中，小五星教学法的Python语言的学习页面
说明：
'''
@study.route('/smallfivestar')       
def smallfivestar():    
    return render_template('study/py_s_fivestar.html')

'''
日期:2024-01-26
作者:陈军
完成状态：
功能描述：路由,任务页面
说明：
'''
@study.route('/task')
def task_style():
    return render_template('study/task.html')

'''
日期:2024-01-26
作者:陈军
完成状态：
功能描述：路由,键盘练习页面
说明：
'''
@study.route('/key')       
def key():    
    return render_template('study/key.html')


'''
日期:2024-01-26
作者:陈军
完成状态：
功能描述：路由,协作编程页面；
说明：需要启动yjs的服务器，目前只有一个通道
'''
@study.route('/yjs')
def yjs():
    return render_template('study/yjs.html')

'''
日期:2024-01-26
作者:陈军
完成状态：
功能描述：路由,阅读项目代码页面；
说明：需要启动yjs的服务器，目前只有一个通道
'''
@study.route('/snap')
def snap():
    return render_template('study/snap.html')   

'''
日期:2024-01-26
作者:权鹏
完成状态：未完成
功能描述：路由,新闻的页面；
说明：每个页面都有不同的操作
'''
@study.route('/news')
def read_news():
    return render_template('study/news.html')

'''
日期:2024-01-26
作者:熊泽
完成状态：未完成
功能描述：路由,论坛页面；
说明：每个页面都有不同的操作
'''
@study.route('/forum')
def forum():
    return render_template('study/forum.html')

'''
日期:2024-01-26
作者:陈军
完成状态：
功能描述：路由,一个标准的五星学习法的页面；
说明：每个页面都有不同的操作
'''
@study.route('/fivestar')       
def fivestar():    
    return render_template('study/fivestar.html')

'''
日期:2024-01-26
作者:陈军
完成状态：
功能描述：路由,一个标准的五星学习法的页面；
说明：每个页面都有不同的操作
'''
@study.route('/back')
def back_style():
    return render_template('study/back.html')   



