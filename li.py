#!/usr/bin/env python3
import os
import psycopg2
#conn = psycopg2.connect("host='sm-pgdb06-dba.dave.net-a-porter.com' dbname='photolib' user='stef' password='pass'")
conn = psycopg2.connect("host='192.168.1.103' dbname='photolib' user='stef' password='pass'")
cursor = conn.cursor()
print("Connected!\n")
rootDir='/media/s.munn/My Passport/Pictures'
rootDir='/home/s.munn/elitedesk'
rootDir='/home/s.munn/dev'
rootDir='/home/s.munn/Desktop/master/dev'
rootDir='/media/stef/Seagate Backup Plus Drive/2003'
source='sbpd2003'
rootDir='/run/user/1000/gvfs/smb-share:server=stef-hp-elitedesk-800-g1-sff.local,share=users'
source='desk20210313'
rootDir='/media/stef/Seagate Backup Plus Drive'
source='sbpd'
rootDir='/media/stef/My Passport/everything/master-42.3GB'
source='red_everything_master42'
rootDir='/media/stef/My Passport/everything/var-2'
source='red_everything_master_var-2'

#for dirName, subdirList, fileList in os.walk(rootDir,followlinks=false):
for dirName, subdirList, fileList in os.walk(rootDir):
#   print(dirName)
   for fname in fileList:
#      print(dirName + '/' + fname)
      
#      path = dirName + '/' + fname
#      if os.path.islink(path)
#         continue
      statinfo = os.stat(dirName + '/' + fname)
      query = "insert into photo(src,dr,nm,url,sz) values (%s, %s, %s, %s, %s);"
      data = (source, dirName, fname, dirName + '/' + fname, statinfo.st_size)
      cursor.execute(query, data)
      conn.commit()


