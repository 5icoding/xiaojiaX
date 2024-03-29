from utils.pool import db_pool
import pymysql


class SQLHelper(object):
    def __init__(self):
        self.conn = None
        self.cursor = None

    def open(self, cursor=pymysql.cursors.DictCursor):
        self.conn = db_pool.pool.connection()
        self.cursor = self.conn.cursor(cursor=cursor)

    def close(self):
        self.cursor.close()
        self.conn.close()

    def fetchone(self, sql, params):
        cursor = self.cursor
        print(sql, params)
        name = 'learner1'
        #select * from users where username='learner1';
        sql1 = """select * from users where username = {}""".format(name)
        cursor.execute(sql1)
        result = cursor.fetchone()

        return result

    def fetchall(self, sql, params):
        cursor = self.cursor
        cursor.execute(sql, params)
        result = cursor.fetchall()
        return result

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
