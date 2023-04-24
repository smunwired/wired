#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql as mdb
import time
from datetime import datetime, timedelta
import sys

con = mdb.connect(host='localhost', user='testuser', password='test623', database='testdb')

with con:
    
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS writers")
    cur.execute("CREATE TABLE writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 name VARCHAR(25))")
    cur.execute("INSERT INTO writers(name) VALUES('Jack London')")
    cur.execute("INSERT INTO writers(name) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO writers(name) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO writers(name) VALUES('Emile Zola')")
    cur.execute("INSERT INTO writers(name) VALUES('Truman Capote')")

    con.commit()
