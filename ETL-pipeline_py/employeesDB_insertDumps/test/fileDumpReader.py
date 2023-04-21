import asyncio
import os
#import pandas as pd
import json
import multidict
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


DB_NAME = "Sample33"

dirPathName = "./ETL-pipeline_py/employeesDB_insertDumps/test"  #for your directory value if specified outside current directory/ if your script is in the same directory as your files then you can put empty string quotes(""), your current directory will be used.

def use_DBNAME ():
    #try-catch and initiate the SQL sever to USE the DB_NAME or create a new DB using the create_database function if not DB_NAME does not exist
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("error on DB_NAME: {}".format(err.msg))

## list out all the names of the metadata files in the given directory.
def filesPathList ():
        #get a list of all file name from specified path using the listdir funct.
        dirPath = dirPathName
        currentDir = os.curdir #print current directory (essentially a dot)
        DirFileNames=[]
        if (dirPath == ""):
                osPath= os.listdir(path =f"{currentDir}")
                for p in osPath:
                        if (p.endswith(".txt")): #check for intended file name(in this case only files ending with text(.txt) format)
                               DirFileNames.append((p))
        else:
                osPath= os.listdir(path =f"{dirPath}")
                for p in osPath:
                        if (p.endswith(".txt")): #check for intended file name(in this case only files ending with text(.txt) format)
                                        DirFileNames.append((p))

        return DirFileNames
print(filesPathList())
##Define the a new logic to read files names in a preferred order and preferred files.
def tableInsertOrder ():
       ##A LOGIC is defined to handle the insert of the dataset into the database in a particular order due to the define constraints on the tables (e.g. the foreign key ON DELETE constraints between table )

        #store the list of the insert data file names from directory
        insertFiles = filesPathList()

        #preferred order to handle DB tables constraints
        #insert order preference/ all table values defined in this Dict must exist in the list of file names from the directory in use.
        insertOrder = {}
        insertOrder[1] = "employees"
        # insertOrder[2] = "departments"
        # insertOrder[3] = "dept_manager"
        # insertOrder[4] = "salaries1"
        # insertOrder[5] = "dept_emp"
        # insertOrder[6] = "titles"

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

dirPath = dirPathName
InsertsToTables =  tableInsertOrder ()
for tableInsert in InsertsToTables:
                fileName = f"{tableInsert}.txt"
                print(tableInsert)
                capsTable_name = tableInsert.upper()
                if (dirPath == ""):
                        filePath= fileName
                        openFile = open(filePath, "r")
                        readFile = f"{(openFile.read())}".split("\n")
                        fileValues =" ".join(readFile)
                        print(fileValues)
                        try:
                                        print("Inserting {} dataset into database...".format(capsTable_name))
                                        query = "INSERT INTO `{table}` VALUES {val};".format(table= tableInsert, val=fileValues )
                                        cursor.execute (query)
                        except mysql.connector.Error as err:
                                        print("Error inserting data into {table} table: {err}".format(table=capsTable_name, err=err.msg))
                        else: print("Successfully imported {} data".format(capsTable_name))
                else:
                        filePath= f"{dirPath}/{fileName}"
                        openFile = open(filePath, "r")
                        readFile = openFile.read().split(",\n")
                        chunkCount=(round(len(readFile)/30000))
                        rowsCount= 0
                        chunkList={}
                        valueCounter = 1
                        for i in range(0, chunkCount, 1):
                                #with await as asyncio:\
                                valueCounter = 1
                                chunkValue = readFile[rowsCount : (rowsCount + 30000)]
                                fileValues= ",".join(chunkValue)
                                chunkList[valueCounter] = fileValues
                                print(f"chunklist:{len(chunkList)}")
                                rowsCount = rowsCount+30001
                                print(rowsCount)
                                for list in chunkList:
                                        try:
                                                                cnx = mysql.connector.connect(**config)
                                                                cursor = cnx.cursor()
                                                                use_DBNAME()
                                                                print("Inserting {} dataset into database...".format(capsTable_name))
                                                                query = "INSERT INTO `{table}` VALUES {val};".format(table= tableInsert, val= chunkList[valueCounter] )
                                                                cursor.execute (query)
                                                                cnx.commit()
                                                                cursor.close()
                                        except mysql.connector.Error as err:
                                                                print("Error inserting data into {table} table: {err}".format(table=capsTable_name, err=err.msg))
                                        else:
                                                print("Successfully imported {} data".format(capsTable_name))
                                                valueCounter = valueCounter+1

                                cnx.close()
openFile.close()
print("Closing {} database connection".format(DB_NAME.upper()))
# cursor.close()
# cnx.close()