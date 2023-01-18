"""
The module comprises of the driver program to read all files, folders, sub-folders, and sub-files within a directory.
It also comprises of the functions which read a directory and handle exceptions.
"""

import os
import csv

b = ' bytes'                                    # String to be used in displaying summary of records 
f = ' files'                                    # String to be used in displaying summary of records
header = ["Path", "Folders/Subfiles", "Files"]  # Header to be displayed in summary of records


def walk_error_handler(exceptionInstance: FileNotFoundError)-> None:
    """
    Handles the errors when user inserts an invalid directory path.

    Parameters
    ----------
    exceptionInstance : FileNotFoundError
        The recorded exception.

    Returns
    -------
    None
        
    """
    
    print("The path does not exist")


def record_data(path: str, onerror = walk_error_handler)-> None:
    """
    Recursively reads all folders, files, subfolders, and subfiles within a directory and records in a csv file.

    Parameters
    ----------
    path : str
        The directory path to be read.

    onerror : function
        The error handler.

    Returns
    -------
    None
        
    """

    headerDisplay = 0        # Value used to check if the header should be displayed                    
    foldersDict = dict()
    subfilesDict = dict()
    recordsFile = open('/home/ekkelai/Desktop/data.csv', 'w')
    for directory, folders, file in os.walk(path, onerror=walk_error_handler):
        foldersDict.clear()
        subfilesDict.clear()
        fileWriter = csv.writer(recordsFile)
        incrementCount = lambda x: x + 1        # Function used to increment value of headerDisplay
        if incrementCount(headerDisplay) == 1: fileWriter.writerow(header)
        for folder in folders:
            subfilesList = []
            if folder:
                numberofFiles = 0
                items = os.listdir(os.path.join(directory,folder))     # All items in a directory being recorded
                for item in items:
                    if os.path.isfile(os.path.join(directory,folder,item)):
                        subfilesList.append(item)
                        numberofFiles += 1
                amount = (str(numberofFiles) + ' files')
                if subfilesList:
                    subfiles = ', '.join(map(str,subfilesList)) 
                    subfilesDict[subfiles] = amount
                else:
                    subfilesDict["-"] = amount
        foldersDict = {folder: data for (folder, data) in zip(folders, subfilesDict.items())} 
        filesDict = {f: str((os.stat(os.path.join(directory, f)).st_size)) + b for f in file}
        directoryData = [directory, foldersDict, filesDict]
        fileWriter.writerow(directoryData)
        headerDisplay += 1
    recordsFile.close()
    with open('/home/ekkelai/Desktop/data.csv') as recordsFile:
        fileReader = csv.reader(recordsFile)
        for record in fileReader:
            print(" ".join(record))


if __name__ == '__main__':
    directory = input('Enter directory\n')
    record_data(directory)
