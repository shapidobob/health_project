import psycopg2
import pymysql
from datetime import datetime

# database connection
#connection = pymysql.connect(host="localhost", port=8889, user="root", passwd="root", database="SELECTION_DB")
#cursor = connection.cursor()
# some other statements  with the help of cursor
#connection.close()

def connect(dtb, usr, hst, password, port):
    #connection = pymysql.connect(host=hst, port=port, user=usr, passwd=password, database=dtb)
    #return connection
    conn = psycopg2.connect(database = dtb, 
                            user = usr, 
                            host= hst,
                            password = password,
                            port = port)
    return conn

def addmember(conn,Fname, Lname, Birthday, Weight, Resting_Heart_Rate, Blood_Pressure, Payment_Info, Email):
    cur = conn.cursor()
    cmd = "INSERT INTO members(Fname, Lname, Birthday, Weight, Resting_Heart_Rate, Blood_Pressure, Payment_Info, Email) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
    cur.execute(cmd, (Fname, Lname, Birthday, Weight, Resting_Heart_Rate, Blood_Pressure, Payment_Info, Email))
    conn.commit()
    cur.close()


def updatemember(conn, Fname, Lname, Birthday, Weight, Resting_Heart_Rate, Blood_Pressure, Payment_Info, Email, ID):
    cur = conn.cursor()
    cmd = "UPDATE members SET Fname = %s, Lname = %s, Birthday = %s, Weight = %s, Resting_Heart_Rate = %s, Blood_Pressure = %s, Payment_Info = %s, Email = %s WHERE Member_ID = %s"
    cur.execute(cmd, (Fname, Lname, Birthday, Weight, Resting_Heart_Rate, Blood_Pressure, Payment_Info, Email, ID))
    conn.commit()
    cur.close()

def addgoal(conn, Member_ID, Metric, Value):
    cur = conn.cursor()
    cmd = "INSERT INTO goals(Member_ID, Metric, Value) VALUES(%s,%s,%s);"
    cur.execute(cmd, (Member_ID, Metric, Value))
    conn.commit()
    cur.close()

def updategoal(conn,Goal_ID, Metric, Value):
    cur = conn.cursor()
    cmd = "UPDATE members SET Metric = %s, value = %s WHERE Goal_ID = %s"
    cur.execute(cmd, (Metric, Value, Goal_ID))
    conn.commit()
    cur.close()

def addactivity(conn, Member_ID, Date, Num_Minutes, Activity):
    cur = conn.cursor()
    cmd = "INSERT INTO activities(Member_ID, Date, Num_Minutes, Activity) VALUES(%s,%s,%s);"
    cur.execute(cmd, (Member_ID, Date, Num_Minutes, Activity))
    conn.commit()
    cur.close()

def addtrainer(conn, Fname, Lname, Email):
    cur = conn.cursor()
    cmd = "INSERT INTO trainers(Fname, Lname, Email) VALUES(%s,%s,%s);"
    cur.execute(cmd, (Fname, Lname, Email))
    conn.commit()
    cur.close()


def addsession(conn, Room_Number, Instructor_ID, Start_Time, End_Time, Activity, Capacity):
    cur = conn.cursor()
    cmd = "SELECT * FROM sessions WHERE Instructor_ID = %s OR Room_Number = %s;"
    cur.execute(cmd, (Instructor_ID,Room_Number))
    rows = cur.fetchall()
    conn.commit()
    for row in rows:
        if (row[3] <= datetime.strptime(End_Time, '%Y-%m-%d %H:%M:%S')) and (row[3] >= datetime.strptime(Start_Time, '%Y-%m-%d %H:%M:%S')):
            return False
        elif(row[4] <= datetime.strptime(End_Time, '%Y-%m-%d %H:%M:%S')) and (row[4] >= datetime.strptime(Start_Time, '%Y-%m-%d %H:%M:%S')):
            return False
    cur = conn.cursor()
    cmd = "INSERT INTO sessions(Room_Number, Instructor_ID, Start_Time, End_Time, Activity, Capacity) VALUES(%s,%s,%s,%s,%s,%s);"
    cur.execute(cmd, (Room_Number, Instructor_ID, Start_Time, End_Time, Activity, Capacity))
    conn.commit()
    cur.close()
    return True

def changesession(conn, Room_Number, Instructor_ID, Start_Time, End_Time, Activity, Capacity, Session_ID):
    cur = conn.cursor()
    cmd = "SELECT * FROM sessions WHERE Instructor_ID = %s OR Room_Number = %s;"
    cur.execute(cmd, (Instructor_ID,Room_Number))
    rows = cur.fetchall()
    conn.commit()
    for row in rows:
        if (row[3] <= datetime.strptime(End_Time, '%Y-%m-%d %H:%M:%S')) and (row[3] >= datetime.strptime(Start_Time, '%Y-%m-%d %H:%M:%S')):
            return False
        elif(row[4] <= datetime.strptime(End_Time, '%Y-%m-%d %H:%M:%S')) and (row[4] >= datetime.strptime(Start_Time, '%Y-%m-%d %H:%M:%S')):
            return False
    cur = conn.cursor()
    cmd = "UPDATE sessions SET Room_Number=%s, Instructor_ID=%s, Start_Time=%s, End_Time=%s, Activity=%s, Capacity=%s WHERE Session_ID = %s;"
    cur.execute(cmd, (Room_Number, Instructor_ID, Start_Time, End_Time, Activity, Capacity, Session_ID))
    conn.commit()
    cur.close()
    return True

def searchmembers(conn, Fname, Lname):
    cur = conn.cursor()
    cmd = "SELECT * FROM members WHERE Fname = %s AND Lname = %s;"
    cur.execute(cmd, (Fname,Lname))
    rows = cur.fetchall()
    conn.commit()
    return rows

def getpayment(conn, Fname, Lname):
    cur = conn.cursor()
    cmd = "SELECT Payment_Info FROM members WHERE Fname = %s AND Lname = %s;"
    cur.execute(cmd, (Fname,Lname))
    rows = cur.fetchall()
    conn.commit()
    return rows

def booksession(conn, Member_ID, Session_ID):
    cur = conn.cursor()
    cmd = "SELECT * FROM sessions WHERE Session_ID = %s;"
    cur.execute(cmd, (Session_ID))
    rows = cur.fetchall()
    conn.commit()
    if len(rows) == 0:
        return False
    for row in rows:
        cap = row[6]
    cur = conn.cursor()
    cmd = "SELECT * FROM bookings WHERE Session_ID = %s;"
    cur.execute(cmd, (Session_ID))
    rows = cur.fetchall()
    conn.commit()
    if len(rows) == cap:
        return False
    cur = conn.cursor()
    cmd = "INSERT INTO bookings(Member_ID, Session_ID) VALUES(%s,%s);"
    cur.execute(cmd, (Member_ID,Session_ID))
    conn.commit()
    cur.close()
    return True

def checkmaintenance(conn):
    cur = conn.cursor()
    cmd = "SELECT * FROM machines ORDER BY Last_Maintenance ASC;"
    cur.execute(cmd)
    rows = cur.fetchall()
    conn.commit()
    return rows
