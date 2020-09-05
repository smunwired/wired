#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import time
from datetime import datetime, timedelta

con = mdb.connect('192.168.0.70', 'stef', 'pass', 'mydb')
p0 = raw_input("enter mod, del or defaults to new : ") or "new"
p1 = raw_input("enter date, y for yesterday, defaults to today : ") or time.strftime("%Y-%m-%d")
p2 = raw_input("enter text, make it legendary: ")
#p3 = raw_input("enter dist : ")
#p4 = raw_input("enter av : ")
#p5 = raw_input("enter max : ")
#p6 = raw_input("enter odo : ")
#p7 = raw_input("enter notes : ")

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
        if p1=="y":
            d = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        else:
            d = p1
        t = p2
        sql="""insert into paragr(dt,txt) values (%s,%s)"""
        cur.execute(sql, (d,t))
        #cur.execute("insert into fence (str) values (%s,);",
        #(d,))
        print "Number of rows inserted:",  cur.rowcount
