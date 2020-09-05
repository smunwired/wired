#!/usr/bin/python2.7
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='test1' user='test1' host='192.168.56.103' password='test1'")
    cur = conn.cursor()
    cur.execute("""select datname from pg_database""")
    rows = cur.fetchall()
    print "\nShow me the databases:\n"
    for row in rows:
        print "  ", row[0]
except:
    print "I am unable to connect to the database"
