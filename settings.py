#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis


class BaseConfig(object):
    SESSION_TYPE = 'redis'  # session类型为redis
    SESSION_KEY_PREFIX = 'session:'  # 保存到session中的值的前缀
    SESSION_PERMANENT = False  # 如果设置为True，则关闭浏览器session就失效。
    SESSION_USE_SIGNER = False  # 是否对发送到浏览器上 session:cookie值进行加密

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/sites?charset=utf8"
                                             #数据库用户名:密码@host:port/数据库名?编码
    SQLALCHEMY_POOL_SIZE = 2
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = -1

    # 追踪对象的修改并且发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass