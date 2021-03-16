import os
import psycopg2
conn = psycopg2.connect("host='192.168.1.103' dbname='photolib' user='stef' password='pass'")
cursor = conn.cursor()
print("Connected!\n")
rootdir = '/media/stef/My Passport/everything/sandisk64_20191008'
source = 'red_everything_sandisk'
for dirName,subdirList, fileList in os.walk(rootdir):
#	print('Found directory: %s' % dirName)
   for fname in fileList:
#		print('\t%s' % fname)  
      path=os.path.join(dirName, fname)
      if os.path.islink(path):
         print('skipping path ' + path)
         continue
      statinfo = os.stat(dirName + '/' + fname)
      query = "insert into photo(src,dr,nm,url,sz) values (%s, %s, %s, %s, %s);"
      data = (source, dirName, fname, dirName + '/' + fname, statinfo.st_size)
      cursor.execute(query, data)
      conn.commit()

