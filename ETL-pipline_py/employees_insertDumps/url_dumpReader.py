import os
import pandas as pd
import json

#get a list of all file name from dumpfolder funct.
osPath= os.listdir(path ="./ETL-pipline_py/employees_insertDumps")

for queryFiles in osPath:
    filePath= f"./ETL-pipline_py/employees_insertDumps/{queryFiles}"
    openFile = open(filePath, "r")
    readFile = openFile.read()
    print(str(readFile))
    openFile.close()

#df = pd.DataFrame()"r"