import pymysql

import os


class ProductsResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():
        usr = os.environ.get("DBUSER")
        pw = os.environ.get("DBPW")
        h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

        return conn

    @staticmethod
    def get_products_list(limit, offset):
        sql="SELECT * FROM commerce1.products ORDER BY product_id LIMIT %s OFFSET %s;" % (limit, offset)
        print(sql)
        conn = ProductsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = list(cur.fetchall())

        return result


    @staticmethod
    def get_products_by_id(key):

        sql = "SELECT * FROM commerce1.products where product_id=%s"
        conn = ProductsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

