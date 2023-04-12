import os
from typing import Counter
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

DB_NAME = "sample12"

def use_DBNAME ():
    #try-catch and initiate the SQL sever to USE the DB_NAME or create a new DB using the create_database function if not DB_NAME does not exist
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("error on DB_NAME: {}".format(err))


def filesPathList ():
        #get a list of all file name from specified path using the listdir funct.
        currentDir = os.curdir #print current directory (essentially a dot)
        osPath= os.listdir(path =f"{currentDir}")#/ETL-pipeline_py/employeesDB_insertDumps")
        DirFileNames=[]
        for p in osPath:
                #osPathList= list(p)
                DirFileNames.append((p))

        return DirFileNames

use_DBNAME()
table_name= "dept_emp"

def tableInsertOrder (table_name):
       ##A LOGIC is defined to handle the insert of the dataset into the database in a particular order due to the define constraints on the tables (e.g. the foreign key ON DELETE constraints between table )
         
         #preferred order to handle DB tables constraints
        insertOrder = {}
        insertOrder[1] = "employees"
        insertOrder[2] = "departments"
        insertOrder[3] = "dept_manager"
        insertOrder[4] = "dept_emp"
        insertOrder[5] = "salaries"
        insertOrder[6] = "titles"

        #relist table_name properly
        tableName ={}

        for i in range (1, max(insertOrder)+ 1, 1) :
                counter = 1
                for inOrder in insertOrder:
                       if(inOrder[counter]== table_name):
                              tableName.append(inOrder[counter])
                              counter = counter + 1
                      
        return tableName


print(filesPathList())
InsertsToTables = filesPathList()
for tableInsert in InsertsToTables:
        fileName = f"{table_name}.txt"
        capsTable_name = table_name.upper()
        counter = 1
        if (tableInsert == fileName, table_name == "employees"):
                filePath= fileName#= f"./ETL-pipeline_py/employeesDB_insertDumps/{fileName}"
                openFile = open(filePath, "r")
                readFile = openFile.read()
                try:
                        print("Inserting {} dataset into database...".format(capsTable_name))
                        cursor.execute(readFile)
                except mysql.connector.Error as err:
                        print("Error inserting data into {table} table: {err}".format(table=capsTable_name, err=err.msg))
                else: print("Successfully imported {} data".format(capsTable_name))
                print("Closing {} database connection".format(DB_NAME.upper()))
openFile.close()




cursor.close()
cnx.close()