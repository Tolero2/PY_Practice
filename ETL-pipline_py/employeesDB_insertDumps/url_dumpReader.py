import os
import pandas as pd
import json

#get a list of all file name from dumpfolder funct.
osPath= os.listdir(path ="./ETL-pipline_py/employeesDB_insertDumps")

for queryFiles in osPath:
    filePath= f"./ETL-pipline_py/employeesDB_insertDumps/{queryFiles}"
    openFile = open(filePath, "r")
    readFile = openFile.read()

    for table_name in TABLES:
        try:
            print("Inserting {} data into database...".format(table_name))
            cursor.execute(readFile)
        except MYSQL.connector.error as err:
            print("error inserting data into {} table".format(table_name))
        print(str(readFile))
openFile.close()

