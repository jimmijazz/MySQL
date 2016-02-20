#Setting up local MySQL Server#
#Start MySQL in System Preferences
#Run Mamp -> Start Servers
#Ensure correct port is being used.

#Set Database Configs
user="root"
password="password"
host="localhost"
port="8889"
database="mysql"

import mysql.connector
from mysql.connector import Error

#connect to database
def connect():
    try:
        conn = mysql.connector.connect(user=user,password=password,host=host,port=port,database=database)
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()

if __name__ == '__main__':
    connect()
