#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

uId = 1
uPrice = 55500 

try:
     
    con = psycopg2.connect("dbname='testdb' user='janbodnar'") 
    
    cur = con.cursor()
    
    cur.execute("select tran_id,to_char(tran_date,\'yyyy-mm-dd\') tran_date,tran_creditor,regexp_replace(tran_desc,'\"',' inch') tran_desc,"


    cur.execute("UPDATE Cars SET Price=%s WHERE Id>%s", (uPrice, uId))        
    con.commit()
    
    print "Number of rows updated: %d" % cur.rowcount
    
   

except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
