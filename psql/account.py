#!/usr/bin/python

import MySQLdb
import psycopg2
db = MySQLdb.connect("localhost","stef","pass","mydb" )
con = None
con = psycopg2.connect("dbname='trxndb' user='trxnuser'") 
mcursor = db.cursor()
pcur = con.cursor()
pcur.execute("select account_id,account_name from account order by account_id")

# Fetch all the rows in a list of lists.
#qSQLresults = cursor.fetchall()
qSQLresults = pcur.fetchall()
for row in qSQLresults:
    id = row[0]
    nm = row[1]

    #SQL query to INSERT a record into the table FACTRESTTBL.
    mcursor.execute('''INSERT into account (account_id, account_name )
                  values (%s, %s)''',
                  (id, nm))

    # Commit your changes in the database
    db.commit()

# disconnect from server
db.close()