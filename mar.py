#!/usr/bin/python 
import mysql.connector as mariadb 
mariadb_connection = mariadb.connect(host='192.168.0.11', user='stef', password='pass', database='mydb') 
cursor = mariadb_connection.cursor()
