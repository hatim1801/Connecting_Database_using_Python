# import library
import psycopg2

# create a connection to a database
try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=4040")
except psycopg2.Error as e:
    print("Error:could not make connection")
    print(e)

# creating cluster that we can use to make queries
try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error:could not get cursor")
    print(e)

# Set automatic commit to be true so that each action is committed without having to call conn.commit() after each command.
conn.set_session(autocommit=True)

# create a database
try:
    cur.execute("create database myfirstdb")
except psycopg2.Error as e:
    print(e)

# close the current connection
try:
    conn.close()
except psycopg2.Erroe as e:
    print(e)

# create a new connection
try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=myfirstdb user=postgres password=4040")
except psycopg2.Error as e:
    print("Error:could not connect")
    print(e)

# creating a cursor
try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print(e)

#commit
conn.set_session(autocommit=True)

#create a table
try: 
    cur.execute("CREATE TABLE IF NOT EXISTS students (student_id int, name varchar,\
    age int, gender varchar, subject varchar, marks int);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)

# insert values
try: 
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks) \
                 VALUES (%s, %s, %s, %s, %s, %s)", \
                 (1, "Raj", 23, "Male", "Python", 85))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO students (student_id, name, age, gender, subject, marks) \
                  VALUES (%s, %s, %s, %s, %s, %s)",
                  ( 2, "Priya", 22, "Female", "Python", 86))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

# Validate your data was inserted into the table.
try: 
    cur.execute("SELECT * FROM students;")
except psycopg2.Error as e: 
    print("Error: select *")
    print (e)

row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

# finally close
cur.close()
conn.close()
