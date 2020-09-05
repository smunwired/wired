#!/usr/bin/python2.7
import psycopg2
try:
    conn=psycopg2.connect("dbname='test1' user='test1' password='test1' host='192.168.56.102'")
    print "connected"
except:
    print "db connection failed but I am giving you no detail, sucker!"

cur = conn.cursor()

try:
    cur.execute("""SELECT * from trn""")
except:
    print "I can't SELECT from trn"

rows = cur.fetchall()
for row in rows:
    print row
