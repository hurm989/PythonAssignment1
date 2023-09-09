# 1. open_folder(path, folder_name)
# 2. move_to_parent_folder(path)
# 3. display_files_and_folder(path)
# 
# the task is to
# print all files of folder_3
# print all files of folder_1

# while calling open_folder function you can use hardcoded value for folder_name argument i.e folder_3
# hint: use os.path.join, os.path.abspath, os.getcwd, os.listdir
# no need to use loop

import os

path=os.getcwd()

def open_folder(path, folder_name):
    newPath=os.path.join(path,folder_name)
    return newPath

def move_to_parent_folder(newPath):
    pathTwo=os.path.join(newPath,"..","..")
    return pathTwo

def display_files_and_folder(pathTwo):
    pathThree=os.listdir(pathTwo)
    return pathThree


# FILES OF FOLDER 3
# openFolder=open_folder(path,"folder3")
# allFiles=display_files_and_folder(openFolder)
# print(allFiles)


# FILES OF FOLDER 1
# parentFolder=move_to_parent_folder(path)
# list=display_files_and_folder(parentFolder)
# print(list)