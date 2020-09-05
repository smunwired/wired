#!/usr/bin/python

# This one reads a postgres database, stores in an array and writes to mysql.

import MySQLdb
import psycopg2

# Open database connection
db = MySQLdb.connect("localhost","stef","pass","mydb" )

con = None
con = psycopg2.connect("dbname='trxndb' user='trxnuser'") 

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
pcur.execute("select tran_id,to_char(tran_date,\'yyyy-mm-dd\') tran_date,tran_creditor,regexp_replace(tran_desc,'\"',' inch') tran_desc,"
"tran_amount,cr_dr,tran_type_id,account_id,to_char(statement_date,'yyyy-mm-dd') statement_date,cheque_no,receipt_ind,dd_ind,"
"to_char(date_created,'yyyy-mm-dd hh24:mi:ss') date_created,user_created,to_char(date_amended,\'yyyy-mm-dd hh24:mi:ss\') date_amended,"
"user_amended,frequency,cred_id,branch_id,cost_code from transdet order by tran_id")

# Fetch all the rows in a list of lists.
#qSQLresults = cursor.fetchall()
qSQLresults = pcur.fetchall()
for row in qSQLresults:
    tid = row[0]
    trd = row[1]
    trc = row[2]
    dsc = row[3]
    amt = row[4]
    crdr = row[5]
    ttyd = row[6]
    accd = row[7]
    std = row[8]
    chq = row[9]
    rcpt = row[10]
    dd = row[11]
    dtc = row[12]
    usc = row[13]
    dta = row[14]
    usa = row[15]
    frqd = row[16]
    crdd = row[17]
    brnd = row[18]
    ccdd = row[19]

    #SQL query to INSERT a record into the table FACTRESTTBL.
    mcursor.execute('''INSERT into transdet (tran_id, tran_date, tran_creditor, tran_desc, tran_amount, cr_dr, tran_type_id, account_id, statement_date, cheque_no, receipt_ind, dd_ind, date_created, user_created, date_amended, user_amended, frequency, cred_id, branch_id, cost_code )
                  values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                  (tid, trd, trc, dsc, amt, crdr, ttyd, accd, std, chq, rcpt, dd, dtc, usc, dta, usa, frqd, crdd, brnd, ccdd))

    # Commit your changes in the database
    db.commit()

# disconnect from server
db.close()
