#!/usr/bin/python2.7
import sys
#import MySQLdb
import mysql.connector
#from magic import Connect #Private mysql connect information - I COMMENTED THIS LINE to use direct connection
#db = MySQLdb.connect(host="192.168.0.23", # your host, usually localhost
#db = mysql.connector.connect(host="192.168.56.103", # your host, usually localhost
#                     user="stef", # your username
#                      passwd="pass", # your password
#                      db="mydb") # name of the data base
db = mysql.connector.connect(user='stef', password='pass', database='mydb')
dbc = db.cursor()

import psycopg2

#dbx=Connect()
#DB=psycopg2.connect("dbname='test1'")
DB = psycopg2.connect("dbname='test2' user='test1' host='192.168.56.101' password='test1'")
DC=DB.cursor()

mysql='''show tables from mydb'''
dbc.execute(mysql); ts=dbc.fetchall(); tables=[]
for table in ts: tables.append(table[0])
for table in tables:
    mysql='''describe mydb.%s'''%(table)
    dbc.execute(mysql); rows=dbc.fetchall()
    psql='drop table %s'%(table)
    try:
	print psql
        DC.execute(psql); DB.commit()
    except psycopg2.Error as e: 
	#print "Unable to connect!"
        #print e.pgerror
        #print e.diag.message_detail
        #sys.exit(1)
	print e.pgerror	
	DB.commit()
	pass

    psql='create table %s ('%(table)
    for row in rows:
        name=row[0]; type=row[1]
        if 'int' in type: type='int8'
        if 'blob' in type: type='bytea'
        if 'datetime' in type: type='timestamptz'
        if 'float' in type: type='float'
        psql+='%s %s,'%(name,type)
    psql=psql.strip(',')+');'
    print psql
    try: DC.execute(psql); DB.commit()
    #except: pass
    except psycopg2.Error as e: 
	print e.pgerror
	sys.exit(1)

    msql='''select * from mydb.%s'''%(table)
    dbc.execute(msql); rows=dbc.fetchall()
    n=len(rows); print n; t=n
    if n==0: continue #skip if no data

    cols=len(rows[0])
    for row in rows:
        ps=', '.join(['%s']*cols)
        psql='''insert into %s values(%s)'''%(table, ps)
        DC.execute(psql,(row))
        n=n-1
        if n%1000==1: DB.commit(); print n,t,t-n
    DB.commit()
