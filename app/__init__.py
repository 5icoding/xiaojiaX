from flask import Flask, jsonify,g
from utils.pool.sqlhelper import SQLHelper

from .views.site import site
from .views.account import account
from .views.study import study
from .views.course import course
from .views.coding import coding
from .views.menu import menu

from .views.auth import auth
from .views.pert import pert

from .views.design import design

from .extensions import db

from flasgger import Swagger



def create_app():
    app = Flask(__name__, instance_path="/tmp" ,static_folder='static',static_url_path='')
    
    app.config['SECRET_KEY'] = '365818fd398f1bc6db5743907791d6c067e9c8362a8d742d74c6e1c811f2abbf'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@localhost:3306/sites'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.debug = True

    #swagger = Swagger(app)

    db.init_app(app)

    #注册蓝图
    app.register_blueprint(site)
    app.register_blueprint(account)
    app.register_blueprint(study)
    
    app.register_blueprint(course)
    app.register_blueprint(coding)

    app.register_blueprint(auth)
    app.register_blueprint(menu)
    app.register_blueprint(pert)
    
    app.register_blueprint(design)

    app.add_url_rule("/", endpoint="site.index")
    
    return app