import mysql.connector as con


obj = con.connect(
    user='root',
    password='Pantera@101',
    host='localhost',
    database="PROJECT"
)

cur1 = obj.cursor()

q1 = "select * from student"

cur1.execute(q1)
print(cur1.fetchall())
