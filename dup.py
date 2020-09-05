#!/usr/bin/env python
import os
import psycopg2
from pathlib import Path
conn = psycopg2.connect("host='192.168.56.105' dbname='dupdb' user='stef' password='pass'")
cursor = conn.cursor()
print "Connected!\n"
rootDir='/media/stef/Seagate Backup Plus Drive/aapic'
source='blue'
#rootDir='/home/stef/aapic'
#rootDir='/media/stef/My Passport/zzpic'
#rootDir='/home/stef/oPictures'
#source='Pictures'
#source='red'
rootDir='/mnt/zed/Pictures'
source='zed'
rootDir='/mnt/mycloud/Shared Pictures'
source='mycloud'
rootDir='/home/stef/Pictures'
source='Pictures40'
source='My Passport'
rootDir='/media/s.munn/My Passport/Pictures'
source='DUP2'
rootDir='/home/s.munn/Desktop_DUP2'
try:
    for dirName, subdirList, fileList in os.walk(rootDir):
       print(dirName)
       for fname in fileList:
          print(dirName + '/' + fname)
          statinfo = os.stat(dirName + '/' + fname)
          query = "insert into dup(src,dr,nm,url,sz,sfx) values (%s, %s, %s, %s, %s, %s);"
          data = (source, dirName, fname, dirName + '/' + fname, statinfo.st_size, Path(fname).suffix)
          cursor.execute(query, data)
          conn.commit()
except:
    pass


