#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql as mdb

con = mdb.connect(host='localhost', user='testuser', password='test623', database='testdb');

with con: 

    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")

    rows = cur.fetchall()

    for row in rows:
        print(row)
