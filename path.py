#photolib=# create table filelist(src text,url text,dr text,nm text, sz bigint, created timestamp default now()) partition by list(src);
#CREATE TABLE
#photolib=# create table filelist_documents_p partition of filelist for values in ('documents');
#CREATE TABLE
#!/usr/bin/python

import sys, getopt
import os
import psycopg2
from datetime import date

def main(argv):
   rootdir = ''
   table = ''
   partition = ''
   try:
       opts, args = getopt.getopt(argv,"d:r:t:p:",["dbhost=","rootdir=","table=","partition="])
   except getopt.GetoptError:
      print( 'test.py -d <database host> -r <rootdir> -t <table> -p <partition>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print( 'test.py -d <database host> -r <rootdir> -t <table> -p <partition>')
         sys.exit()
      elif opt in ("-d", "--dbhost"):
         dbhost = arg
      elif opt in ("-r", "--rootdir"):
         rootdir = arg
      elif opt in ("-t", "--table"):
         table = arg
      elif opt in ("-p", "--partition"):
         partition = arg
   print( 'Database host is "', rootdir)
   print( 'Source directory is "', rootdir)
   print( 'Destination table is "', table)
   print( 'Destination partition is "', partition)

   conn = psycopg2.connect("host=" + dbhost + " dbname=photolib user=stef password=pass")
   cursor = conn.cursor()
   print("Connected!\n")
   query = "truncate table " + table + "_" + partition + "_p";
   cursor.execute(query)
   print('source label : ' + partition + ' , path : ' + rootdir )
   for dirName,subdirList, fileList in os.walk(rootdir):
#	print('Found directory: %s' % dirName)
     for fname in fileList:
#		print('\t%s' % fname)  
        path=os.path.join(dirName, fname)
        if os.path.islink(path):
           print('skipping path ' + path)
           continue
        statinfo = os.stat(dirName + '/' + fname)
        query = "insert into " + table + "(src,dr,nm,url,sz,created) values (%s, %s, %s, %s, %s, %s);"
        data = (partition, dirName, fname, dirName + '/' + fname, statinfo.st_size, date.today())
        cursor.execute(query, data)
        conn.commit()


if __name__ == "__main__":
   main(sys.argv[1:])
