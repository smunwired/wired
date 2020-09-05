#!/usr/bin/env python
import MySQLdb
p0=raw_input("enter year defaults to 2020 : ") or 2020
yr='0000'
mn='00'
dy='00'
db = MySQLdb.connect(host="192.168.56.101", user="stef", passwd="pass", db="mydb")
cursor = db.cursor()
x = 'apples'
y = 'lemons'
z = "In the basket are %s and %s" % (x,y)
fn="%s.txt" % (p0,)
tweets = open(fn, "w") 
cursor.execute( """SELECT  date_format(dt,'%%Y') as yr,
    date_format(dt,'%%M') as mn,
    dt,
    concat(date_format(dt,'%%W'),\" \",date_format(dt,'%%D')) as dy, replace(txt,'<br/>','\n') as txt, md 
        FROM paragr where date_format(dt,'%%Y')=%s order by dt""", (p0,))
for row in cursor:
    if row[0] != yr:
        print>>tweets, row[0]
        yr = row[0]
    if row[1] != mn:
        print>>tweets, row[1]
        mn = row[1]
    if row[3] != dy:
        print>>tweets, row[3]
        dy = row[2]
    print>>tweets, row[4], row[5]
tweets.close()
db.close()

