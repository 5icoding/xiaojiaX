from app.extensions import db


"""
日期：2024-01-20
作者:陈军
功能描述：等级过关条件类，基于SQLAlchemy实现
说明：开发者设定，作为等级过关的判断条件，conditions是一个字符串-》类型，数量；。。。；类型，数量
"""

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.Integer)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))  
    
