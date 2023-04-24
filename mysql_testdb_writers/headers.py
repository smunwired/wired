#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql as mdb

con = mdb.connect(host='localhost', user='testuser', password='test623', database='testdb')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Writers LIMIT 5")

    rows = cur.fetchall()

    desc = cur.description

    print("%s %3s" % (desc[0][0], desc[1][0]))

    for row in rows:    
        print("%2s %3s" % row)
