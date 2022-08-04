# read data from mysql, database= ineuron, table = fitbit

import mysql.connector as conn


mydb = conn.connect(host='localhost', user='root', passwd='susant123', database='ineuron' )
#print(mydb.is_connected())  # checking database connection
cursor= mydb.cursor()
'''
#fetch available tables
cursor.execute("show tables")
records = cursor.fetchall()
l = []
for i in records:
    l.append(i)
print(l)'''

# fetch records from database

cursor.execute("select * from fitbit")
records_fit = cursor.fetchall()
for i in records_fit:
    print(i)