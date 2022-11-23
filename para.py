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

with con:

    cur = con.cursor()
    if p1=="y":
      d = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    else:
      d = p1
    t = p2
    sql="""insert into paragr(dt,txt) values (%s,%s)"""
    cur.execute(sql, (d,t,))
    con.commit()
    print("Number of rows inserted:",  cur.rowcount)
