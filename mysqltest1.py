# creating a database that is nexleaf
import mysql.connector as conn
mydb = conn.connect(host='localhost', user='root', passwd='susant123')
# checking the connection is establish or not
print(mydb.is_connected())

# creating a cursor object by using cursor()
cursor = mydb.cursor()

#creating database by sql queries
cursor.execute('create database if not exists nexleaf5')
cursor.execute('show databases')
print(cursor.fetchall())
