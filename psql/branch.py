#!/usr/bin/python

import MySQLdb
import psycopg2
db = MySQLdb.connect("localhost","stef","pass","mydb" )
con = None
con = psycopg2.connect("dbname='trxndb' user='trxnuser'") 
mcursor = db.cursor()
#mcursor.execute("drop table if exists branch")
mcursor.execute("create table brn (brnd smallint, brn varchar(100) not null)")
pcur = con.cursor()
pcur.execute("select branch_id id, branch_name nm from branch order by branch_id")


# Fetch all the rows in a list of lists.
#qSQLresults = cursor.fetchall()
qSQLresults = pcur.fetchall()
for row in qSQLresults:
    id = row[0]
    nm = row[1]

    #SQL query to INSERT a record into the table FACTRESTTBL.
    mcursor.execute('''INSERT into brn (brnd, brn )
                  values (%s, %s)''',
                  (id, nm))

    # Commit your changes in the database
    db.commit()

# disconnect from server
db.close()
