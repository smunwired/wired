#!/usr/bin/env python
import datetime
import mysql.connector

cnx = mysql.connector.connect(user='stef', password='pass', host='192.168.56.101', database='employees')
cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(1999, 1, 1)
#hire_end = datetime.date(2999, 12, 31)
hire_end = raw_input("hire_end")
print hire_end
cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()
cnx.close()

