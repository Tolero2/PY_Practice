import os
import pandas as pd
import json

#get a list of all file name from dumpfolder funct.
osPath= os.listdir(path ="./ETL-pipline_py/employees_insertDumps")

for queryFiles in osPath:
    filePath= f"./ETL-pipline_py/employees_insertDumps/{queryFiles}"
    openFile = open(filePath, "r")
    readFile = openFile.read()

    for table_name in TABLES:
        try:
            print("Inserting {} data into database...".format(table_name))
        print(str(readFile))
openFile.close()

