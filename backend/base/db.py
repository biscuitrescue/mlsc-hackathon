import mysql.connector as con


obj = con.connect(
    user='root',
    password='Pantera@101',
    host='localhost',
    database='PROJECT'
)


cur1 = obj.cursor()
