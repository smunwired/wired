#!/usr/bin/env python
import MySQLdb
p0=input("max price")
db = MySQLdb.connect(host="192.168.56.101", user="stef", passwd="pass", db="mydb")

c=db.cursor()
max_price=15
c.execute("""SELECT dt FROM paragr WHERE date_format(dt,%s) = %s""", ("%Y",p0,))
result=c.fetchall()


for row in result:
  print row[0]
c.close()

