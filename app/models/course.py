from app.extensions import db

"""
日期：2024-01-？
作者:陈军
功能描述：课程类，基于SQLAlchemy实现
说明：临时课程，是代码存储为js的一个测试类
"""
class TmpCourse(db.Model):
    __tablename__ = 'tmp_courses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parentId = db.Column(db.Integer)
    title = db.Column(db.String(50))
    description = db.Column(db.String(50))
    filePath = db.Column(db.String(50))
    createTime = db.Column(db.DateTime)
    sequence = db.Column(db.Integer)

"""
日期：2024-01-21
作者:陈军
功能描述：课程类，基于SQLAlchemy实现
相关类：
"""
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parentId = db.Column(db.Integer)
    level = db.Column(db.Integer)
    title = db.Column(db.String(50))
    category = db.Column(db.String(50))
    description = db.Column(db.String(50))
    code = db.Column(db.Text)
    createTime = db.Column(db.DateTime)

"""
日期：2024-01-21
作者:陈军
功能描述：课程单元类，基于SQLAlchemy实现
相关类：
"""
class CourseUnits(db.Model):
    __tablename__ = 'course_units'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    levelId = db.Column(db.Integer)
    courseId = db.Column(db.Integer)
    sequence = db.Column(db.Integer)
    title = db.Column(db.String(50))

    target = db.Column(db.String(255))
    content = db.Column(db.String(255))
    codeExample = db.Column(db.Text)
    exercise = db.Column(db.String(255))
    exerciseCode = db.Column(db.Text)

    createTime = db.Column(db.DateTime)
    description = db.Column(db.String(50))


