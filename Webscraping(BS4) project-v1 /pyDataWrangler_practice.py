#I will attempt to read, clean and append crypto pricing data that I webscrapped and stores in 6 different file; some of which are indexed and some are not. The files also come in two formats(CSV and JSON). the goal is to have these 6 files consolidated into one excel file and saved down for analysis.

#importing the modules I would use for parsing and cleaning the files
from argparse import FileType
from operator import index
import pandas as pd
import json
import csv
import time
from pathlib import Path



#define the data path(s) and store it in a variable
generalPath = '[YOUR GENERAL DIRECTORY]' #source folder
#file_nth = Path(f"{generalPath}/[YOUR CSV FILE NAME]") #csv
file1 = Path(f"{generalPath}/[df_practice/noIndex.csv]") #csv
file2 = Path(f"{generalPath}/df_practice/yet_another_path_noIndex.csv") #csv
file3 = Path(f"{generalPath}/yet_another_path_noIndex.csv") #csv
file4 = Path(f'{generalPath}/first_test.csv') #csv
file5 = Path(f"{generalPath}/test_2_noIndex.csv") #csv
#OR all files can be grouped directly to a list
fileGroupCSV= [
    Path(f"{generalPath}/df_practice/noIndex.csv")
    ,Path(f"{generalPath}/df_practice/yet_another_path_noIndex.csv")
    ,Path(f"{generalPath}/yet_another_path_noIndex.csv")
    ,Path(f'{generalPath}/first_test.csv'), Path(f"{generalPath}/test_2_noIndex.csv")
] #ALL CSV FILES IN A LIST

fileJSON = Path(f'{generalPath}/crypto_blob_azure_job.json') #json

#USING THE GROUPED CSV FILES IN A LIST SO THAT I CAN LOOP IT THROUGH THE READER FUNCTIONS
def csvFilesReader(fileGroupPath):
    #READING INDIVIDUAL CSV FILE AS ONE RECORD AND STORING IT IN A LIST, THEN READ THE LIST OF LIST  AND APPEND IT TO THE TEMPLATE ARRAY ATTRIBUTES.
    allRecordsList = []
    csvFinalRecordList = {"RANK":[], "NAME": [], "SYMBOL": [], "PRICE($)": [], "VOLUME": [], "MARKETCAP": [], "EventProcessedDate": [] }#Dict Template for Array of attributes

    for eachFile in fileGroupPath:
        csvReader = pd.read_csv(eachFile)
        eachRecord= csvReader.to_dict("records")
        allRecordsList.append(eachRecord)
        for recordsList in allRecordsList:
            for records in recordsList:
                csvFinalRecordList["RANK"].append(records["RANK"])
                csvFinalRecordList["NAME"].append(records["NAME"])
                csvFinalRecordList["SYMBOL"].append(records["SYMBOL"])
                csvFinalRecordList["PRICE($)"].append(records["PRICE($)"])
                csvFinalRecordList["VOLUME"].append(records["VOLUME"])
                csvFinalRecordList["MARKETCAP"].append(records["MARKETCAP"])
                csvFinalRecordList["EventProcessedDate"].append("2023-02-16") #manual date entry to back fill the csv file data with missing date

    csvtoRecords = pd.DataFrame( csvFinalRecordList).to_dict("records") #read to dataframe for easy outputing (records in this case)

    return csvtoRecords



#FUNCTION TO READ AND CLEAN THE PARSED JSON AND OUTPUT THE INTENDED COLUMNS FOR THIS PRODUCT  (i.e. EventProcessedDate )
def azure_jsonFile_cleaner(fileJSON1):
    jsonFile = pd.read_json(fileJSON1, lines= True)
    #CREATE A NEW DATA FRAME TO SELECT ONLY WANTED COLUMNS FROM THE PARSED RAW JSON INPUT
    dfSpecific= pd.DataFrame(jsonFile, columns= ["RANK","NAME","SYMBOL","PRICE($)", "VOLUME","MARKETCAP","EventProcessedUtcTime"])

    # SPLIT COLUMN(EventProcessedUtcTime) TO GET SPECIFIC DATE VALUE SEPARATED FROM TIME VALUE AND STORE IN NEW COLUMNS(EventProcessedDate, EventProcessedTime)
    dfSpecific[["EventProcessedDate", "EventProcessedTime"]] = dfSpecific["EventProcessedUtcTime"].str.split( pat='T', expand=True)

    #DROPPING THE UNWANTED COLUMN(EventProcessedUtcTime) AND COLUMN(EventProcessedTime) AND SETTING THE AXIS TO CHECK AS 1 OR 'COLUMNS' AND COMMITTING THE CHANGE TO THE DF WITH inplace = True
    dfSpecific.drop(["EventProcessedTime", "EventProcessedUtcTime" ], axis=1,inplace=True)
    jsonFinalRecordsList =  dfSpecific.to_dict("records")

    return jsonFinalRecordsList


#FINAL CONSOLIDATED  AND FORMATTED TABLE TO BE SENT TO TABLEAU FOR DATA VISUALIZATION
def consolidatedFiles():
    #FINAL DATAFRAME TEMPLATE THAT WILL HOLD THE CONSOLIDATED DATA OF THE SAME ROWS FROM THE DIFFERENT FILES(i.e. CSV and JSON)
    RANK = []
    NAME= []
    SYMBOL= []
    PRICE = []
    VOLUME = []
    MARKETCAP =[]
    EventProcessedDate = []

    #call the File(JSON and CSV) cleaner functions and save their output in a list with aim to run iterable transformation on both files
    outputList= [ azure_jsonFile_cleaner(fileJSON),csvFilesReader(fileGroupCSV)]
    for eachlist in outputList:
          for list in eachlist:
                 RANK.append(list["RANK"])
                 NAME.append(list["NAME"])
                 SYMBOL.append(list["SYMBOL"])
                 PRICE.append(list["PRICE($)"])
                 VOLUME.append(list["VOLUME"])
                 MARKETCAP.append(list["MARKETCAP"])
                 EventProcessedDate.append(list["EventProcessedDate"])
    #PRINT DATAFRAME TABLE SCHEMA
    df = pd.DataFrame(columns = ["RANK", "NAME", "SYMBOL","PRICE($)","VOLUME","MARKETCAP", "EventProcessedDate" ])
    df["RANK"]= RANK
    df["NAME"]= NAME
    df["SYMBOL"]= SYMBOL
    df["PRICE($)"]= PRICE
    df["VOLUME"]= VOLUME
    df["MARKETCAP"]= MARKETCAP
    df["EventProcessedDate"]= EventProcessedDate
    df.to_excel(excel_writer= 'final_weekly_crypto_data', sheet_name= "sheet1", index=False)
    return df


consolidatedFiles()













