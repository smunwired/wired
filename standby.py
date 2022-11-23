#!/usr/bin/python
# -*- coding: utf-8 -*-

#import MySQLdb as mdb
import pymysql as mdb
import time
from datetime import datetime, timedelta
import sys

con = mdb.connect(host=sys.argv[1], user='stef', password='pass', database='mydb')
p0 = input("enter mod, del or defaults to new : ") or "new"
p1 = input("enter date, y for yesterday, defaults to today : ") or time.strftime("%Y-%m-%d")
p2 = input("enter text, make it legendary: ")
p3 = input("enter additional overtime hours : ")
p4 = input("enter standby ind : ")
p5 = input("enter rate : ")

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
        t = p2
        h = p3
        s = p4
        r = p5
        sql="""insert into standby(dt,hrs,txt,stby,rt) values (%s,%s,%s,%s,%s)"""
        cur.execute(sql, (d,h,t,s,r))
        con.commit()
        print("Number of rows inserted:",  cur.rowcount)
