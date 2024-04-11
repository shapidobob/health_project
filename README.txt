connect(dtb, usr, hst, password, port)
  used to create the CONN variable used in other functions

addmember(conn,Fname, Lname, Birthday, Weight, Resting_Heart_Rate, Blood_Pressure, Payment_Info, Email)
  adds a new member

updatemember(conn, Fname, Lname, Birthday, Weight, Resting_Heart_Rate, Blood_Pressure, Payment_Info, Email, ID)
  can change any info for a member selected by ID

addgoal(conn, Member_ID, Metric, Value)
  adds a goal for the member such as walk(min) 100 being walk 100 minutes

updategoal(conn,Goal_ID, Metric, Value)
  changes goal data

addactivity(conn, Member_ID, Date, Num_Minutes, Activity)
  allows members to log activities. entering what activity was preformed on what day and for how long

addtrainer(conn, Fname, Lname, Email)
  creates a new trainer

addsession(conn, Room_Number, Instructor_ID, Start_Time, End_Time, Activity, Capacity)
  checkes if instructor and room is free then creates a session capacity is 1 for a one on one session or higher for a class

changesession(conn, Room_Number, Instructor_ID, Start_Time, End_Time, Activity, Capacity, Session_ID)
    checkes for any new conflicts then modifies session info

searchmembers(conn, Fname, Lname)
    searches for a member by name

getpayment(conn, Fname, Lname)
    searches by name to get payment info

booksession(conn, Member_ID, Session_ID)
    checkes that session exists and is not full before adding a booking

checkmaintenance(conn)
    showes a list of all machines sorted by when they were last maintained
