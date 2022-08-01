# databse = nexleaf
import mysql.connector as conn
import csv
mydb = conn.connect(host='localhost',  user='root', database='nexleaf', passwd='susant123')
cursor = mydb.cursor()

# sql queries to create a table
attribute_query ="create table if not exists attribute(Dress_ID int(10), Style varchar(80),	Price varchar(80),	Rating float(20),	Size varchar(10),	Season varchar(30),	NeckLine varchar(30),	SleeveLength	varchar(30), waiseline	varchar(30), Material	varchar(30), FabricType varchar(30),	Decoration	varchar(30), Pattern_Type	varchar(30), Recommendation int(10))"

# executing sql command
cursor.execute(attribute_query)

# reading the csv file and inserting into table
with open('attribute1.csv',"r") as data :
    next(data)
    data_csv = csv.reader(data, delimiter= "\n")
    print(data_csv)
    for i in enumerate(data_csv):
        print(i)
        for j in i[1] :
            print(type(j))
            cursor.execute('insert into attribute values ({data})'.format(data=(j)))
    print("all the data inserted ")
mydb.commit()

'''

with open('attribute1.csv',"r") as data :
    next(data)
    data_csv = csv.reader(data, delimiter= "\n")
    print(data_csv)
    for j in data_csv:
        cursor.execute(f'insert into attribute values (str(j[0]))')
    print("all the data inserted ")
mydb.commit() '''

'''
# read csv file and inserting into table
with open('attribute1.csv', 'r') as fp:
    next(fp)
    attr_data = csv.reader(fp, delimiter="\n")
    #print(attr_data)
    for i in attr_data:
        print(type(i))
        print(i)
        cursor.execute("insert into attribute values ({data})".format(data=(str(i[0]))))
        #cursor.execute(f'insert into attribute3 values({data})'.format(data=(str(i[0]))))

print('Data inserted done')
conn.close()
mydb.commit()'''

'''
,,,

with open('data_many.json') as file:
    file_data = json.load(file)
collection.insert_many(file_data)
'''