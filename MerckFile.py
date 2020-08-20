#!/usr/bin/env python
# coding: utf-8

# In[19]:


import os
import csv
import copy
import sys
import glob
import re
import pymssql
import pandas as pd
'''
    For the given path, get the List of all files in the directory tree 
'''
server = '172.30.9.242'
username = 'developde'
password = 'everyday@123'
conn = pymssql.connect(host=server,user=username,password=password,database="DWMedProStaging")
cursor = conn.cursor()

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        
def main():
    
    dirName = 'D:\\FileReading\\Satip\\'
    #listA=[]
    #counter=0
    # Get the list of all files in directory tree at given path
    #listOfFiles = getListOfFiles(dirName)
    
    # Print the files
    #for elem in listOfFiles:
        #print(elem)
    #print ("****************")
    
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for foldernames in os.listdir(dirName):
        #listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        #print(dirName+foldernames)
        FileFullPath=dirName+foldernames
        #print(FileFullPath)
        print(foldernames)
        
        # Using re.split()  
        # Splitting characters in String  
        res = re.split('_', foldernames) 
        #print(str(res))
        startdate=res[1]
        enddate=res[2]
        #print(startdate)
        #print(enddate)
        print ("****************")
        for filename in os.listdir(dirName+foldernames):
            
            #print(filename)
            #result=[i for i in glob.glob('EH_Response*.{}'.format("txt"))]
            #print(result)
            if 'EH_Response' in filename:
                #print(filename)
                result=filename
                #print(result)
                #count = len(open(result).readlines())
                count = 0
                with open(FileFullPath+"\\"+result, 'r') as f:
                    #reader = txt.reader(f)
                    for line in f:
                        count += 1
                    #print(count)
                    FolderPathFile=FileFullPath+"\\"+result
                    #print(FolderPathFile)
                sql1 = "INSERT INTO %s (filename,RecordCount,startdate,enddate,fullfilepath) VALUES ('%s',%s,'%s','%s','%s');" % ('dwmedprostaging..tbAudit_File_TEST_04', result,count,startdate,enddate,FolderPathFile)
                #print(sql1)
                #cursor.execute('Truncate table dwmedprostaging..tbAudit_File_TEST_04')
                cursor.execute(sql1)
                conn.commit()
         

    # Print the files    
    #for elem in listOfFiles:
        #print(elem) 
        
    #print ("****************")   
   
        
if __name__ == '__main__':
    main()


# In[ ]:




