import os
import psycopg2
conn = psycopg2.connect("host='192.168.1.103' dbname='photolib' user='stef' password='pass'")
cursor = conn.cursor()
print("Connected!\n")
rootdir = '/home/stef/dev/how_to_do_stuff_166'
source = 'desk_home_stef'
for dirName,subdirList, fileList in os.walk(rootdir):
   if "snap" in subdirList:
      subdirList.remove("snap")
#   print('Found directory: %s' % dirName)
   for fname in fileList:
#      print('\t%s' % fname)
      path=os.path.join(dirName, fname)
      if os.path.islink(path):
         print('skipping path ' + path)
         continue
      statinfo = os.stat(dirName + '/' + fname)
      query = "insert into photo(src,dr,nm,url,sz) values (%s, %s, %s, %s, %s);"
      data = (source, dirName, fname, dirName + '/' + fname, statinfo.st_size)
      cursor.execute(query, data)
      conn.commit()

