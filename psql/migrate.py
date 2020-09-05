#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
import MySQLdb as mdb



con = None

try:
     
    con = psycopg2.connect("dbname='trxndb' user='trxnuser'") 
    con2 = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

    
    cur = con.cursor()     
    cur.execute("select tran_id,to_char(tran_date,\'yyyy-mm-dd\') tran_date,tran_creditor,regexp_replace(tran_desc,'\"',' inch') tran_desc,"
    "tran_amount,cr_dr,tran_type_id,account_id,to_char(statement_date,'yyyy-mm-dd') statement_date,cheque_no,receipt_ind,dd_ind,"
    "to_char(date_created,'yyyy-mm-dd hh24:mi:ss') date_created,user_created,to_char(date_amended,\'yyyy-mm-dd hh24:mi:ss\') date_amended,"
    "user_amended,frequency,cred_id,branch_id,cost_code from transdet order by tran_id limit 10")

    while True:
      
        row = cur.fetchone()
        
        if row == None:
            break
            
        with con2:
    
        	cur = con2.cursor()
        	cur.execute("INSERT INTO transdet(tran_id,tran_date,tran_creditor,tran_desc,tran_amount,cr_dr,tran_type_id,account_id,statement_date,"
        	"cheque_no,receipt_ind,dd_ind,date_created,user_created,date_amended,user_amended,frequency,cred_id,branch_id,cost_code) "
        	"VALUES(" %s " ,'%s','%s','%s',%s,'%s',%s,%s,'%s',%s,%s,%s,'%s','%s','%s','%s',%s,%s,%s,%s),(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19])")
        
        #	print row[0], row[1]
    

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()

