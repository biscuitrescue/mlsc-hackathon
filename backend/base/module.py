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


def conti(w_room, location):
    cur.execute("select * from stand")
    data = cur.fecthall()
    for i in data:
        if i[2] == location:
            driver = i[0]
            ride = {driver: w_room}


def wait(roll):
    w_room = []
    cur.execute("select * from student")
    data = cur.fetchall()

    for i in data:
        if i[1] == roll:
            w_room.append(roll)
            location = i[2]

    if len(w_room) <= 4:
        pass

    t1 = threading.Thread(lambda: sleep(30))
    t2 = threading.Thread(conti, args=(w_room, location))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
