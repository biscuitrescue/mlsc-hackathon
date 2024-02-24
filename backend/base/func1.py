import mysql.connector as con


obj = con.connect(
    user='root',
    password='<pass>',
    host='localhost',
    database='PROJECT',
)

cur = con.cursor()

def assign(dest):
    pass
