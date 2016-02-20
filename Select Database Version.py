#!/usr/bin/python

user="root"
password="password"
host="localhost"
port="8889"
database="mysql"

import mysql.connector
from mysql.connector import Error

#connect to database
db = mysql.connector.connect(user=user,password=password,host=host,port=port,database=database)
#Initialize Cursor
cursor = db.cursor()
#execute SQL query
cursor.execute("SELECT VERSION()")
#Fetch single row
data= cursor.fetchone()

print("Database version: %s " % data)

db.close()
