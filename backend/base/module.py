from time import sleep
import threading
import mysql.connector as con

obj = con.connect(
    user='root',
    password='Pantera@101',
    host='localhost',
    database="PROJECT"
)

cur = obj.cursor()

cur.execute("select * from student")


def conti(roll, id):
    pass

def wait(roll, id):
    data = cur.fetchall()
    for i in data:
        if i[1] == roll:
            t1 = threading.Thread(lambda: sleep(30))
            t2 = threading.Thread(conti, args=(roll, id))

            t1.start()
            t2.start()

            t1.join()
            t2.join()
