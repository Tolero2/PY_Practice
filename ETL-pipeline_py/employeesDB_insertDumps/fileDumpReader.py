from ast import Or
import os
import pandas as pd
import json
import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': 'root1234',
  'host': '127.0.0.1',
  #'raise_on_warnings': True #FOR DEVELOPER'S USE ONLY
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

DB_NAME = "sample17"

def use_DBNAME ():
    #try-catch and initiate the SQL sever to USE the DB_NAME or create a new DB using the create_database function if not DB_NAME does not exist
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("error on DB_NAME: {}".format(err))

## list out all the names of the metadata files in the given directory.
def filesPathList ():
        #get a list of all file name from specified path using the listdir funct.
        currentDir = os.curdir #print current directory (essentially a dot)
        osPath= os.listdir(path =f"{currentDir}/ETL-pipeline_py/employeesDB_insertDumps")
        DirFileNames=[]
        for p in osPath:
                #osPathList= list(p)
                DirFileNames.append((p))

        return DirFileNames

use_DBNAME()
##Define the a new logic to read files names in a preferred order and preferred files.
def tableInsertOrder ():
       ##A LOGIC is defined to handle the insert of the dataset into the database in a particular order due to the define constraints on the tables (e.g. the foreign key ON DELETE constraints between table )

        #store the list of the insert data file names from directory
        insertFiles = filesPathList()

        #preferred order to handle DB tables constraints
        #insert order preference/ all table values defined in this Dict must exist in the list of file names from the directory in use.
        insertOrder = {}
        insertOrder[1] = "employees"
        insertOrder[2] = "dept_manager"
        insertOrder[3] = "departments"
        insertOrder[4] = "salaries1"
        insertOrder[5] = "departments"
        insertOrder[6] = "titles"

        # serialize tableName to hold table_name list in the insert order preference
        tableName = {}

        for insertTable in insertFiles:
                for keyOrder in insertOrder:
                        if (f"{insertOrder[keyOrder]}.txt" == insertTable):
                                 tableName[keyOrder] = f"{insertOrder [keyOrder]}"

        #return the list of table names in the insert order preference as a list variable
        orderedTableName = []
        counter = 1 # counter to help reorder the dict values using key matching(n)
        for i in range(0, len(insertOrder), 1):
                orderedTableName.append(tableName[counter])
                counter = counter + 1
        return orderedTableName

print(tableInsertOrder())


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
#                 if (tableInsert == fileName):
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




# cursor.close()
# cnx.close()

# InsertsToTables =  tableInsertOrder ()
# for tableInsert in InsertsToTables:
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
# openFile.close()




# cursor.close()
# cnx.close()