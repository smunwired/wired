#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import time
from datetime import datetime, timedelta

con = mdb.connect('192.168.1.216', 'stef', 'pass', 'mydb')

p0 = input("enter mod, del or defaults to new : ") or "new"
p1 = input("enter date, y for yesterday, defaults to today : ") or time.strftime("%Y-%m-%d")
p2 = input("enter time : ")
p3 = input("enter dist : ")
p4 = input("enter av : ")
p5 = input("enter max : ")
p6 = input("enter odo : ")
p7 = input("enter notes : ")

with con:

    cur = con.cursor()
    if p0=="mod":
        cur.execute("update bike set tm=%s,dst=%s,av=%s,mx=%s,odo=%s,notes=%s where rdate=%s",
        (p2,p3,p4,p5,p6,p7,p1))
        print("Number of rows updated:",  cur.rowcount)
    elif p0=="del":
        cur.execute("delete from bike  where rdate=%s",
        (p1))
        print("Number of rows deleted:",  cur.rowcount)
    else:
        if p1=="y":
            d = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        else:
            d = p1
        cur.execute("insert into bike (rdate,tm,dst,av,mx,odo,notes) values (%s,%s,%s,%s,%s,%s,%s)",
        (d,p2,p3,p4,p5,p6,p7))
        print("Number of rows inserted:",  cur.rowcount)
        con.commit()
