#!/usr/bin/python

# This one reads a postgres database, stores in an array and writes to mysql.

import MySQLdb

import psycopg2

con = None

con = psycopg2.connect("dbname='trxndb' user='trxnuser'") 

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
mcursor = db.cursor()
pcur = con.cursor()

# Select qSQL with id=4.
#cursor.execute("SELECT qSQL FROM TBLTEST WHERE id = 4")
#pcur.execute("SELECT qSQL FROM TBLTEST WHERE id = 4")

# Fetch a single row using fetchone() method.
#results = cursor.fetchone()
#results = pcur.fetchone()

#qSQL = results[0]

#cursor.execute(qSQL)
pcur.execute("select id, city, state from ABC")

# Fetch all the rows in a list of lists.
#qSQLresults = cursor.fetchall()
qSQLresults = pcur.fetchall()
for row in qSQLresults:
    id = row[0]
    city = row[1]

    #SQL query to INSERT a record into the table FACTRESTTBL.
    cursor.execute('''INSERT into FACTRESTTBL (id, city)
                  values (%s, %s)''',
                  (id, city))

    # Commit your changes in the database
    db.commit()

# disconnect from server
db.close()