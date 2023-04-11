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
        osPath= os.listdir(path =f"{currentDir}/ETL-pipeline_py/employeesDB_insertDumps")
        DirFileNames=[]
        for p in osPath:
                #osPathList= list(p)
                DirFileNames.append((p))

        return DirFileNames

use_DBNAME()
table_name= "departments"


InsertsToTables = filesPathList()
for tableInsert in InsertsToTables:
        tableStr = f"{table_name}.txt"
        capsTable_name = table_name.upper()
        if (tableInsert == tableStr):
                filePath= f"./ETL-pipeline_py/employeesDB_insertDumps/{tableStr}"
                openFile = open(filePath, "r")
                readFile = openFile.read()
                try:
                        print("Inserting {} dataset into database...".format(capsTable_name))
                        cursor.execute(readFile)
                except mysql.connector.Error as err:
                        print("Error inserting data into {} table".format(err))
                else: print("Successfully imported {} data".format(capsTable_name))
                print("Closing {} database connection".format(DB_NAME.upper()))
openFile.close()




cursor.close()
cnx.close()