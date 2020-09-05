#!/usr/bin/python2.7
import MySQLdb
import Connect
db = MySQLdb.connect(host="192.168.0.11",user="stef",passwd="pass",db="mydb")
dbx=Connect()
mysql='''show tables from mydb'''
dbx.execute(mysql); ts=dbx.fetchall(); tables=[]
for table in ts: tables.append(table[0])
for table in tables:
    print table
