# insert data to employ table and fetch data , database = nexleaf
import mysql.connector as conn
# establishing the connection
mydb = conn.connect(host='localhost', user='root', database='nexleaf', passwd='susant123')

# creating cursor object by using cursor()
cursor = mydb.cursor()

# sql queries to insert data into te table
emp_data = "insert into employ values(101,'sushanta kumar', 'susant@gmail.com',100000, 30)"

# executing sql queries command
cursor.execute(emp_data)
cursor.execute(emp_data)
cursor.execute(emp_data)
cursor.execute(emp_data)
cursor.execute(emp_data)
cursor.execute(emp_data)
cursor.execute(emp_data)
cursor.execute(emp_data)

# sql queries to fetch data from table
cursor.execute("select * from employ")
record = cursor.fetchall()
for i in record:
    print(i)

print("------------------------------------------")
l = []
for i in record:
    l.append(i)
print(l)
print(type(l))
print(type(l[0]))