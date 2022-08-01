# databse = nexleaf
# create a table attribute
import pandas as pd
import csv
import mysql.connector as conn
mydb = conn.connect(host='localhost', user='root', passwd='susant123')
cursor = mydb.cursor()
cursor.execute('use nexleaf')

# sql queries to create a table
sql_attri = "create table if not exists attribute2(Dress_ID int(10), Style varchar(80),	Price varchar(80),	Rating float(20),	Size varchar(10),	Season varchar(30),	NeckLine varchar(30),	SleeveLength	varchar(30), waiseline	varchar(30), Material	varchar(30), FabricType varchar(30),	Decoration	varchar(30), Pattern_Type	varchar(30), Recommendation int(10))"

# executing sql queries
cursor.execute(sql_attri)


