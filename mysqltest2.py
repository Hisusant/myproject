# creating a employ table in nexleaf database
import mysql.connector as conn
mydb = conn.connect(host='localhost', user='root', database = 'nexleaf', passwd='susant123')

# creating cursor object using cursor()
cursor = mydb.cursor()

# sql query to create a table
sql_query = "create table if not exists employ3(emp_id int(10), emp_name varchar(80), emp_email varchar(30), emp_sal int(30), emp_atten int(10))"
#cursor.execute("create table employ3(emp_id int(10), emp_name varchar(80), emp_email varchar(30), emp_sal int(30), emp_atten int(10))")
cursor.execute(sql_query)
print('Table created')