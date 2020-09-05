#!/usr/bin/python 
import mysql.connector as mdb 
import psycopg2

mconn = mdb.connect(user='test1', password='testp', database='mydb', host='cen7-01') 
mcur = mconn.mcur()

pdb_conn
mysql='''show tables from mydb'''
mcur.execute(mysql); ts=mcur.fetchall(); tables=[]
for table in ts: tables.append(table[0])
for table in tables:
    print table
    mysql='''describe mydb.%s'''%(table)
    mcur.execute(mysql); rows=mcur.fetchall()
    for row in rows:
        name=row[0]; type=row[1];
        if 'int' in type: type='int8'
        if 'blob' in type: type='bytea'
        if 'datetime' in type: type='timestamptz'
        psql+='%s %s,'%(name,type)
    psql=psql.strip(',')+')'
    print psql
    try: DC.execute(psql); DB.commit()
    except: pass

    msql='''select * from w3i.%s'''%(table)
    dbx.execute(msql); rows=dbx.fetchall()
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
