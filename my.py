#!/usr/bin/python2.7
import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='stef',password='pass',
                                host='192.168.56.103',database='mydb')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
