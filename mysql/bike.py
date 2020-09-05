#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import time

con = mdb.connect('localhost', 'stef', 'pass', 'mydb')
p0 = raw_input("enter mod, del or defaults to new") or "new"
p1 = raw_input("enter date or use today") or time.strftime("%Y-%m-%d")
p3 = raw_input("enter dist")
p2 = raw_input("enter time")
p4 = raw_input("enter av")
p5 = raw_input("enter max")
p6 = raw_input("enter odo")
p7 = raw_input("enter notes")
    
with con:    

    cur = con.cursor()
    if p0=="mod":
        cur.execute("update bike set tm=%s,dst=%s,av=%s,mx=%s,odo=%s,notes=%s where rdate=%s",
        (p2,p3,p4,p5,p6,p7,p1))        
        print "Number of rows updated:",  cur.rowcount
    elif p0=="del":
        cur.execute("delete from bike  where rdate=%s",
        (p1))        
        print "Number of rows deleted:",  cur.rowcount
    else:
        cur.execute("insert into bike (rdate,tm,dst,av,mx,odo,notes) values (%s,%s,%s,%s,%s,%s,%s)",
        (p1,p2,p3,p4,p5,p6,p7))        
        print "Number of rows inserted:",  cur.rowcount
