#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

uid = 3

try:
     
    con = psycopg2.connect("dbname='testdb' user='janbodnar'") 
    
    cur = con.cursor()

    cur.execute("SELECT * FROM Cars WHERE Id=%(id)s", {'id': uid } )
    
    print cur.fetchone()
   

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
