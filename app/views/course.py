# -*- coding:utf-8 -*-
import subprocess
import tempfile
import time
from flask import Blueprint, request, render_template, redirect, json
from app.models import TmpCourse
from app.extensions import db
import os
import random
import datetime

course = Blueprint('course', __name__,url_prefix='/course')

@course.route('/',methods=("GET", "POST"))
def read_course():
    if request.method == "POST":

        return redirect('/course/index')

    return render_template('course/index.html')



def productRadFilename():
    # 生成0-100随机数
    num = random.randint(0, 100)
    
    # 获取当前日期和时间
    now = datetime.datetime.now()        
    # 提取年份、月份、日期、小时、分钟和秒数
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    
    # 将结果进行格式化输出
    filename = f"{year}{month}{day}{hour}{minute}{num}"
    return filename

def productFilepath(tmp):
    tmp_file_path=''
    BASE_DIR = os.path.dirname(__file__) 
    tmp_file_path = BASE_DIR[:-6] + tmp
    return tmp_file_path

def productFilePathName():
    filepath = productFilepath('\\tmp\\course') +  "\\" + productRadFilename() +".js"
    return filepath


def  saveCodeToFile(code):
        # 指定文件路径及名称（如果不存在则会自动创建）

        #root_path = request.url_root
        
        BASE_DIR = os.path.dirname(__file__) 

        tmp_file_path = BASE_DIR[:-6]+'\\tmp\\course'
        print(BASE_DIR[:-6]+'\\tmp\\course')
        num = random.randint(0, 100)
        
        # 获取当前日期和时间
        now = datetime.datetime.now()        
        # 提取年份、月份、日期、小时、分钟和秒数
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second
        
        # 将结果进行格式化输出
        filename = f"{year}{month}{day}{hour}{minute}{num}"+'.js'

        filepath =tmp_file_path + "\\"+filename

        print(filepath)
        print('productFilePathName-->'+productFilePathName())

        #filepath = '/file.txt'
        
        # 使用 open() 函数创建或打开文件，设置模式为 'w' 表示写入模式
        with open(filepath, mode='w') as file:
            # 调用 write() 方法将字符串写入文件
            file.write(code)
        
        return filename

@course.route("/create", methods=["GET", "POST"])
def course_create():
    if request.method == "POST":
        #data = json.loads(request.form.get('data')).replace("'", "\"")
        data = request.get_json()
        title = data['title']
        parentId = data['parentId']
        createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        description = data['description']
        code = data['code']
        id=data['id']

        print(code)
        filepath = saveCodeToFile(code)

        print(title,parentId)
        course = TmpCourse(
            title=title,
            parentId=parentId,
            createTime=createTime,
            description=description,
            filePath=filepath,
            sequence = id
        )
        db.session.add(course)
        db.session.commit()
        return 'ok'
        #redirect(url_for("user/create.html", id=user.id))
    return render_template("course/esc_create.html")

# @course.route('/coding',methods=("GET", "POST"))
# def read_coding():
#     return render_template('coding/index.html')

# @course.route('/sequence',methods=("GET", "POST"))
# def read_sequence():
#     return render_template('coding/sequence_diagram.html')


@course.route('/editormd',methods=("GET", "POST"))
def read_editormd():
    return render_template('coding/editormd.html')

@course.route('/uml/class',methods=("GET", "POST"))
def read_uml_class():
    return render_template('coding/uml_class.html')

@course.route('/uml/case',methods=("GET", "POST"))
def read_uml_usecase():
    return render_template('coding/uml_case.html')

@course.route('/uml/sequence',methods=("GET", "POST"))
def read_uml_sequence():
    return render_template('coding/uml_sequence.html')



@course.route('/js',methods=("GET", "POST"))
def js_course():
    return render_template('course/js_ide.html')

@course.route('/py',methods=("GET", "POST"))
def py_course():
    return render_template('course/py_ide.html')

def cmd(command):
    subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    subp.wait(2)
    if subp.poll() == 0:
        print(subp.communicate()[1])
        #return subp.communicate()[1]
    else:
        print("失败")
        #return '网络连接失败，请重试！'


@course.route('/rust',methods=("GET", "POST"))
def rust_course():

    if request.method == 'POST':
        # 获取用户上传的 Rust 代码
        rust_code = request.form['code']
        print(rust_code)

        # 创建临时文件保存 Rust 代码
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.rs', delete=False) as temp_file:
            temp_file.write(rust_code)
            temp_file_path = temp_file.name

        print('temp_file_path->'+temp_file_path)

        try:
            # 构建 Rust 编译和运行命令
            compile_command = ['rustc', temp_file_path]
            run_command = [temp_file_path[:-3]]  # 假设 Rust 文件名为 example.rs

            print(run_command)

            # # 执行 Rust 编译命令
            # result = subprocess.Popen(compile_command, shell=True)
            # result.poll()
            # print(result)

            #cmd(compile_command)

            # # print('run_command'.join(run_command))

            # # # 执行 Rust 运行命令，并捕获控制台输出

            # time.sleep(5)

            # print(run_command)
            
            # result = subprocess.run(run_command, capture_output=True, text=True)

            # time.sleep(5)

            # # 获取控制台输出

            result = subprocess.Popen('C:\\Users\\lenovo\\AppData\\Local\\Temp\\tmpmg2dwkwz', shell=True)
            #result.wait(2)
            #result.poll()
            print('result->')
            print(result)
            # console_output = result.stdout


            

            # time.sleep(15)
            # print('console_output->')
            # print(console_output)

            # cmd = 'dir'
            # ret = subprocess.Popen(cmd, shell=True)
            # ret.poll()
            # print(ret)

            return str(result.stdout)

            #return render_template('result.html', console_output=console_output)

        except subprocess.CalledProcessError as e:
            # 处理编译或运行错误
            error_message = e.stderr
            return render_template('result.html', error_message=error_message)

    return render_template('course/rust_ide.html')

@course.route('/design/js',methods=("GET", "POST"))
def design_js_course():

    if request.method == 'POST':
        return 'post'

    return render_template('course/design_js_course.html')

