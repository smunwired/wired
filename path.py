import os
import psycopg2
from datetime import date
conn = psycopg2.connect("dbname=photolib user=stef password=pass")
cursor = conn.cursor()
print("Connected!\n")
rootdir = '/media/stef/My Passport/everything/sandisk64_20191008'
rootdir = '/media/stef/My Passport/everything/ccnopic'
rootdir = '/media/stef/My Passport/everything/master_DUP'
rootdir = '/media/stef/My Passport/Pictures3'
rootdir='/media/data2/ccpicCANGO20190331'
rootdir='/media/data2/Pictures'
rootdir='/media/data2/saved'
rootdir='/media/data2/Pictures'
rootdir='/media/data2/Music'
rootdir='/data/home/stef/Pictures'
source = 'red_everything_sandisk'
source = 'red_everything_master_dup'
source = 'red_pictures3'
source = 'zedonblue5'
source = 'mdpictures20210531'
source = 'mediadata2music20210531'
source = 'cloud'
source='elitedeskdatahome'
source='pictures20210706'
rootdir='/home/stef/Pictures'
source = 'mediadata220210914'
rootdir = '/media/stef/zed'
rootdir = '/data/home/stef/Documents'
source = 'Documents-data'
rootdir = '/data/home/stef'
source = 'data'
source = 'data2'
rootdir='/media/data2'
print('source label : ' + source + ' , path : ' + rootdir )
for dirName,subdirList, fileList in os.walk(rootdir):
#	print('Found directory: %s' % dirName)
   for fname in fileList:
#		print('\t%s' % fname)  
      path=os.path.join(dirName, fname)
      if os.path.islink(path):
         print('skipping path ' + path)
         continue
      statinfo = os.stat(dirName + '/' + fname)
      query = "insert into filelist(src,dr,nm,url,sz,created) values (%s, %s, %s, %s, %s, %s);"
      data = (source, dirName, fname, dirName + '/' + fname, statinfo.st_size, date.today())
      cursor.execute(query, data)
      conn.commit()

