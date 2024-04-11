import psycopg2
import pymysql

# database connection
#connection = pymysql.connect(host="localhost", port=8889, user="root", passwd="root", database="SELECTION_DB")
#cursor = connection.cursor()
# some other statements  with the help of cursor
#connection.close()

def connect(dtb, usr, hst, password, port):
    connection = pymysql.connect(host=hst, port=port, user=usr, passwd=password, database=dtb)
    return connection
    """conn = psycopg2.connect(database = dtb, 
                            user = usr, 
                            host= hst,
                            password = password,
                            port = port)
    return conn"""

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
    cmd = "INSERT INTO members(Member_ID, Metric, Value) VALUES(%s,%s,%s);"
    cur.execute(cmd, (Member_ID, Metric, Value))
    conn.commit()
    cur.close()

def updategoal(Goal_ID, Metric, Value):
    cur = conn.cursor()
    cmd = "UPDATE members SET Metric = %s, value = %s WHERE Goal_ID = %s"
    cur.execute(cmd, (Metric, Value, Goal_ID))
    conn.commit()
    cur.close()

def addactivity(conn, Member_ID, Metric, Value):
    cur = conn.cursor()
    cmd = "INSERT INTO members(Member_ID, Metric, Value) VALUES(%s,%s,%s);"
    cur.execute(cmd, (Member_ID, Metric, Value))
    conn.commit()
    cur.close()


if __name__ == "__main__":
    conn = connect("health_center","root","localhost","",3306)
    addmember(conn,"Fname", "Lname", '2008-11-11', "200", "70", "20", "testing", "email")
    updatemember(conn,"newname", "Lname", '2008-11-11', "190", "70", "20", "testing", "email", 1)
    