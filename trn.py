#!/usr/bin/python2.7
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='test1' user='test1' host='192.168.56.101' password='test1'")
    cur = conn.cursor()
    try:
        cur.execute("""delete from trn""")
    except:
	print "Delete from trn failed!"
except:
    print "I am unable to connect to the database"
    # insert one row per month for last 20 months
 #   for x in range(-20, 0):
  #      print "var is " % (x)
    #rows = cur.fetchall()
    #print "\nShow me the databases:\n"
    #for row in rows:
    #    print "  ", row[0]
