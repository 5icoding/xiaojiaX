from app.extensions import db

"""
日期：2024-01-20
作者:陈军
功能描述：等级过关条件类，基于SQLAlchemy实现
说明：开发者设定，作为等级过关的判断条件，conditions是一个字符串-》类型，数量；。。。；类型，数量
"""

class SysMenus(db.Model):
    __tablename__ = 'sys_menus'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parentID = db.Column(db.Integer)
    title = db.Column(db.String(50))
    URL = db.Column(db.String(50))

class RoleMenus(db.Model):
    __tablename__ = 'role_menus'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roleId = db.Column(db.Integer)
    parentID = db.Column(db.Integer)
    title = db.Column(db.String(50))
    URL = db.Column(db.String(50))





    
