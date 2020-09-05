#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import time
from datetime import datetime, timedelta

con = mdb.connect('192.168.0.70', 'stef', 'pass', 'mydb')
p0 = raw_input("enter mod, del or defaults to new : ") or "new"
p1 = raw_input("enter date, y for yesterday, defaults to today : ") or time.strftime("%Y-%m-%d")
p2 = raw_input("enter club, defaults to haverstock: ") or "haverstock"
p3 = raw_input("enter text : (optional)") 
p4 = raw_input("enter 1 for lesson, defaults to zero : ") or 0
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
        sql="""insert into fence(dt,venue,txt,lesson) values (%s,%s,%s,%s)"""
        #cur.execute(sql, (d,))
        cur.execute(sql, (d,p2,p3,p4))
        #cur.execute("insert into fence (str) values (%s,);",
        #(d,))
        print "Number of rows inserted:",  cur.rowcount

#MariaDB [mydb]> desc fence;
#+--------+-------------+------+-----+------------+----------------+
#| Field  | Type        | Null | Key | Default    | Extra          |
#+--------+-------------+------+-----+------------+----------------+
#| id     | int(11)     | NO   | PRI | NULL       | auto_increment |
#| dt     | date        | NO   |     | NULL       |                |
#| club   | varchar(44) | NO   |     | haverstock |                |
#| ind    | char(1)     | YES  |     | NULL       |                |
#| lesson | int(11)     | YES  |     | 0          |                |
#+--------+-------------+------+-----+------------+----------------+

