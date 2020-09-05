#!/usr/bin/python

import MySQLdb
import psycopg2
db = MySQLdb.connect("localhost","stef","pass","mydb" )
con = None
con = psycopg2.connect("dbname='trxndb' user='trxnuser'") 
mcursor = db.cursor()
#mcursor.execute("drop table if exists creditor")
#mcursor.execute("create table creditor (ttyd smallint not null primary key, creditor varchar(100) not null")
pcur = con.cursor()
pcur.execute("select creditor_id,creditor from creditor order by creditor_id")

# Fetch all the rows in a list of lists.
#qSQLresults = cursor.fetchall()
qSQLresults = pcur.fetchall()
for row in qSQLresults:
    id = row[0]
    nm = row[1]

    #SQL query to INSERT a record into the table FACTRESTTBL.
    mcursor.execute('''INSERT into creditor (creditor_id, creditor )
                  values (%s, %s)''',
                  (id, nm))

    # Commit your changes in the database
    db.commit()

# disconnect from server
db.close()
