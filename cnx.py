#!/usr/bin/python2.7
import mysql.connector

cnx = mysql.connector.connect(user='test1', password='testp',
                              host='cen7-01',
                              database='mydb')
print "connected"
cnx.close()
