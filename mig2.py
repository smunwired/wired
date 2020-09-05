#!/usr/bin/python2.7
import mysql.connector
db=mysql.connector.connect(user='stef',password='pass',host='192.168.56.103',database='mydb')
mysql='''show tables from mydb'''
db.execute(mysql); ts=db.fetchall(); tables=[]
for table in ts: tables.append(table[0])
for table in tables:
    print table
db.close()
