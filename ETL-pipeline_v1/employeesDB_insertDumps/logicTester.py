
#LOGIC 1

# table_name = ['employees.txt', 'salaries.txt',
#     'dept_emp.txt', 'dept_manager.txt', 'titles.txt', 'departments.txt']
# #insert order preference/ all table values defined in this Dict must exist in the list of file names from the directory in use.
# insertOrder = {}
# insertOrder[1] = "employees"
# insertOrder[2] = "dept_manager"
# insertOrder[3] = "departments"
# insertOrder[4] = "salaries"
# insertOrder[5] = "departments"
# insertOrder[6] = "titles"

# # serialize tableName to hold table_name list in the insert order preference
# tableName = {}

# for table in table_name:
#     for keyOrder in insertOrder:
#         if (f"{insertOrder[keyOrder]}.txt" == table):
#             tableName[keyOrder] = f"{insertOrder                     [keyOrder]}"
# #return the list of table names in the insert order preference as a list variable
# counter = 1 # counter to help reorder the dict values using key matching()
# orderedTableName = []
# for i in range(1, len(insertOrder)+1, 1):
#     orderedTableName.append(tableName[counter])
#     counter = counter + 1
# print(orderedTableName)


##LOGIC 2


# filecont = INSERT INTO `employees` VALUES (10001,'1953-09-02','Georgi','Facello','M','1986-06-26'),
# (10002,'1964-06-02','Bezalel','Simmel','F','1985-11-21'),
# (10003,'1959-12-03','Parto','Bamford','M','1986-08-28'),
# (10004,'1954-05-01','Chirstian','Koblick','M','1986-12-01'),
# (10005,'1955-01-21','Kyoichi','Maliniak','M','1989-09-12'),
# (10006,'1953-04-20','Anneke','Preusig','F','1989-06-02'),
# (10007,'1957-05-23','Tzvetan','Zielinski','F','1989-02-10'),

# #convert the file content from 

# "INSERT INTO `employees` VALUES (10001,'1953-09-02','Georgi','Facello','M','1986-06-26'),(10002,'1964-06-02','Bezalel','Simmel','F','1985-11-21'),(10003,'1959-12-03','Parto','Bamford','M','1986-08-28'),(10004,'1954-05-01','Chirstian','Koblick','M','1986-12-01'),(10005,'1955-01-21','Kyoichi','Maliniak','M','1989-09-12'),(10006,'1953-04-20','Anneke','Preusig','F','1989-06-02'),(10007,'1957-05-23','Tzvetan','Zielinski','F','1989-02-10'),(10008,'1958-02-19','Saniya','Kalloufi','M','1994-09-15'),(10009,'1952-04-19','Sumant','Peac','F','1985-02-18');"


##LOGIC 3
##choose whether you want to insert a single table file data or all table files data. can be specified too by reducing the number of files insert order

# #single table? Y or N
# singleTable = ""
# if (singleTable == "Y"):
#         table_name = " "
#         InsertsToTables =  tableInsertOrder ()
#         for tableInsert in InsertsToTables:
#                 fileName = f"{table_name}.txt"
#                 capsTable_name = table_name.upper()
#                 counter = 1
#                 if (tableInsert == table_name):
#                         filePath= fileName#= f"./ETL-pipeline_py/employeesDB_insertDumps/{fileName}"
#                         openFile = open(filePath, "r")
#                         readFile = openFile.read()
#                         try:
#                                 print("Inserting {} dataset into database...".format(capsTable_name))
#                                 cursor.execute(readFile)
#                         except mysql.connector.Error as err:
#                                 print("Error inserting data into {table} table: {err}".format(table=capsTable_name, err=err.msg))
#                         else: print("Successfully imported {} data".format(capsTable_name))
#                         print("Closing {} database connection".format(DB_NAME.upper()))
#         openFile.close()

# else:

#         #Run the insert query function to populate respective table with its corr file data
#         InsertsToTables =  tableInsertOrder ()
#         for tableInsert in InsertsToTables:
#                 fileName = f"{tableInsert}.txt"
#                 counter = 1
#                 if (tableInsert == fileName):
#                         capsTable_name = str(tableInsert).upper()
#                         filePath= fileName#= f"./ETL-pipeline_py/employeesDB_insertDumps/{fileName}"
#                         openFile = open(filePath, "r")
#                         readFile = openFile.read()
#                         try:
#                                 print("Inserting {} dataset into database...".format(capsTable_name))
#                                 cursor.execute(readFile)
#                         except mysql.connector.Error as err:
#                                 print("Error inserting data into {table} table: {err}".format(table=capsTable_name, err=err.msg))
#                         else: print("Successfully imported {} data".format(capsTable_name))
#                         print("Closing {} database connection".format(DB_NAME.upper()))
#         openFile.close()


##LOGIC 4

import datetime
import os
import pandas as pd
#import MySQLdb
import pymysql as MySQLdb
from sqlalchemy import create_engine

DB_NAME= "SAMPLE35"
tableName= "EMPLOYEES"
file = open(file= "/Users/tobijoshuaayotunde/Documents/GitHub/PY_Practice/ETL-pipeline_py/employeesDB_insertDumps/employees.txt", mode= "r")
fileContent = file.read().splitlines()
sqlBulk = list(fileContent)
attOutput=[]
for att in sqlBulk:
        att1 = att.removeprefix("(")
        att2 = att1.removesuffix("),")
        att3 = att2.removesuffix(")")
        att4 = att3.split(",")
        attOutput.append(att4)

print(attOutput)
engine = create_engine("mysql+pymysql://root:root1234@127.0.0.1:3306/SAMPLE35")
header= pd.read_sql(sql="SELECT * FROM EMPLOYEES", con=engine)
columns= []
for arr in header:
    columns.append(arr)
# print(columns)
firstDF = pd.DataFrame( attOutput, columns=columns )

secondDF= pd.DataFrame(columns=columns)
print(firstDF['emp_no'].conver)
secondDF['emp_no'] = (firstDF['emp_no'])
secondDF['birth_date'] = firstDF['birth_date'].
secondDF['first_name'] = (firstDF['first_name'])
secondDF['last_name'] = (firstDF['last_name'])
secondDF['gender'] = (firstDF['gender'])
secondDF['hire_date'] = datetime.date((firstDF['hire_date']))

val= df.to_csv(path_or_buf="/Users/tobijoshuaayotunde/Documents/GitHub/PY_Practice/ETL-pipeline_py/employeesDB_insertDumps/insertData/{}.csv".format(tableName), mode= "w", index=False ,header=True)
print(secondDF)


config = {
  'user': 'root',
  'password': 'root1234',
  'host': '127.0.0.1',
  'database' : 'SAMPLE35'
  }

conn= MySQLdb.connect(**config)
cursor = conn.cursor()

try:
       cursor.execute("LOAD DATA INFILE '/Users/tobijoshuaayotunde/Documents/GitHub/PY_Practice/ETL-pipeline_py/employeesDB_insertDumps/insertData/EMPLOYEE.csv'insert into EMPLOYEES ")
        # df.to_sql(name="EMPLOYEES", con=engine, index=False, if_exists='append')
except MySQLdb.DatabaseError as err:
        print("Cannot connect: {}".format(err)) 























