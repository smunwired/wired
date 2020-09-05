#!/usr/bin/python2.7
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='test1' user='test1' host='192.168.0.35' password='test1'")
    print "connected!"
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

qstr = "delete from trn"
try:
    cur.execute(qstr)
except:
    print "delete failed"

for x in range(20, 1, -1):
    qtxt = "insert into trn(td,crdd,tamt,ttyp,tact) values (now() - interval '%d month',1,12.34,5,6)" % (x)
    cur.execute(qtxt)

cur.execute("""commit""")

qstr = "select * from trn"
cur.execute(qstr)
rows = cur.fetchall()
for row in rows:
    print row
