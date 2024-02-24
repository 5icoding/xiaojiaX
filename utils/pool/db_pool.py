import time
import pymysql
import threading
from dbutils.pooled_db import PooledDB


# 定义连接参数
pool = PooledDB(
    creator=pymysql,
    maxconnections=6,
    mincached=2,
    maxcached=5,
    blocking=True,
    host='localhost',
    user='root',
    passwd='123456',
    db='sites',
    port=3306,
    charset='utf8mb4'
)