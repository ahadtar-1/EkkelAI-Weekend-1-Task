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

    #recordsFile = open('/home/ekkelai/Desktop/data.csv', 'w')
    #foldersDict = dict()
    for directory, folders, files in os.walk(path, topdown=False, onerror=walk_error_handler):
        #print(folders)
        for folder in folders:
            subfilesList = []
            subfoldersList = []
            print(folder)
            items = os.listdir(os.path.join(directory,folder))
            for item in items:
                if os.path.isfile(os.path.join(directory,folder,item)):
                    subfilesList.append(item)
                else:
                    subfoldersList.append(item)

            print("Fo",subfoldersList)
            print("Fi",subfilesList)


if __name__ == '__main__':
    directory = input('Enter directory\n')
    record_data(directory)
