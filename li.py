#!/usr/bin/env python
import os
import psycopg2
#conn = psycopg2.connect("host='sm-pgdb06-dba.dave.net-a-porter.com' dbname='photolib' user='stef' password='pass'")
conn = psycopg2.connect("host='192.168.56.103' dbname='photolib' user='stef' password='pass'")
cursor = conn.cursor()
print "Connected!\n"
rootDir='/media/s.munn/My Passport/Pictures'
rootDir='/home/s.munn/elitedesk'
rootDir='/home/s.munn/dev'
rootDir='/home/s.munn/Desktop/master/dev'
source='book'
source='else'
source='dev'
source='desk2310'
source='dev20191125'
for dirName, subdirList, fileList in os.walk(rootDir):
#   print(dirName)
   for fname in fileList:
#      print(dirName + '/' + fname)
      statinfo = os.stat(dirName + '/' + fname)
      query = "insert into photo(src,dr,nm,url,sz) values (%s, %s, %s, %s, %s);"
      data = (source, dirName, fname, dirName + '/' + fname, statinfo.st_size)
      cursor.execute(query, data)
      conn.commit()


