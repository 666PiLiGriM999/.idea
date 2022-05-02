import sqlite3
from flask import request

def removing_product():
    productId = request.args.get('productId')
    str = 'DELETE FROM products WHERE productID = ' + productId
    return str

def sql_injection():
    connection = psycopg2.connect("dbname=test user=postgres")
    cur = db.cursor()
    query = removing_product()
    cur.execute(query)
