#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import time
from datetime import datetime, timedelta

con = mdb.connect('localhost', 'stef', 'pass', 'mydb')

with con:

	cursor = con.cursor() 
	icursor = con.cursor() 

	cursor.execute("SELECT id,dt,txt FROM paragr_20180907 order by 1")
	numrows = cursor.rowcount

	rw = 1
	dt = '1000-01-01'
	lst = 'nothing'
	str = 'nothing'


	for x in xrange(0,numrows):
 		row = cursor.fetchone()
		if lst != row[1]:
			#print row[1], str

#			insert into pargra(dt,txt) values (%s,%s)
        		if rw != 1:
        			icursor.execute("insert into paragra(dt,txt) values (%s,%s)", (lst,str))
			else:
        			icursor.execute("insert into paragra(dt,txt) values (%s,%s)", (row[1],str))
			
        		print "Number of rows inserted:",  icursor.rowcount

			lst = row[1]
			str = row[2]
		else:
			str = str + ' ' + row[2]
		rw = rw + 1
#		print str
	print rw
