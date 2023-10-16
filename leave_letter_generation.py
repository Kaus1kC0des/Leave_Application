# Path: leave_letter_generation.py
import sqlite3 as sql
# from sqlite3 import SQLITE_ERROR


# Lets create a python function to insert user input into the leave_letter table

# The table has the following columns:
# regno int,
# name VARCHAR(100),
# rollno VARCHAR(10),
# level VARCHAR(5),
# course VARCHAR(5),
# year INT,
# branch VARCHAR(8),
# section VARCHAR(1),
# total_leave INT,
# reason TEXT,
# leave_from DATE,
# leave_to DATE


# The function will take the following parameters:
# regno,name,rollno,level,course,year,branch,section,total_leave,reason,leave_from,leave_to

# The function will return the following:
# True if the insertion is successful
# False if the insertion is unsuccessful

def insert_into_leave_letter(
regno,
name,
rollno,
course,
year,
level,
branch,
section,
total_leave,
reason,
leave_from,
leave_to
):

    try:
        connection = sql.connect("./content/database.db")
        cursor = connection.cursor()
        cursor.execute(
"INSERT INTO leave_letter VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                regno,
                name,
                rollno,
                course,
                year,
                branch,
                level,
                section,
                total_leave,
                reason,
                leave_from,
                leave_to
            )
        )
        connection.commit()
        connection.close()
        return True
    except Exception as error:
        print(error)
        return False


# gettting user input for the fields
regno = 312322202050
name = "Kausik D"
rollno = "22AM112"
course = "B.Tech"
year = 2
branch = "AIML"
level = "UG"
section = "A"
total_leave = 2
reason = "Fever"
leave_from = "2021-09-01"
leave_to = "2021-09-02"

# calling the function
# insert_into_leave_letter(
#     regno,
#     name,
#     rollno,
#     course,
#     year,
#     level,
#     branch,
#     section,
#     total_leave,
#     reason,
#     leave_from,
#     leave_to
#     )

connection = sql.connect("./content/database.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM leave_letter")
for i in cursor.fetchall():
    print(i)
connection.close()




