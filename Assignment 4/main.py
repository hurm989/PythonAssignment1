# file=open('myFile.txt','r')
# content=file.read()


# contentOne=content.replace("*user*","Hurmat")
# print(contentOne)
# contentOne=contentOne.replace("*title*","Sports")
# print(contentOne)
# contentOne=contentOne.replace("*here*","abc")
# print(contentOne)
# contentTwo=content.replace("*user*","Hur")
# contentTwo=contentTwo.replace("*title*","Movies")
# contentTwo=contentTwo.replace("*here*","abcxyz")
# print(content,contentTwo)
# contentThree=content.replace("*user*","H")
# contentThree=contentThree.replace("*title*","Indoor")
# contentThree=contentThree.replace("*here*","xyz")
# print(content,contentThree)


# userEmail=open("userEmail.txt","a")
# userEmail.write(contentOne+'\n'+contentTwo+'\n'+contentThree)





# # create 3 folders
# # folder_1
# # folder_2
# # folder_3
# # such that folder_3 is inside folder_2 and folder_2 is inside folder_1
# # i.e 
# # folder_1 > folder_2 > folder_3
# # see the image folder_structure.png
# #
# # place some txt files in folder_1 and folder_3
# # place your python program in folder_2 and in the program
# #
# # create 3 functions
# # 1. open_folder(path, folder_name)
# # 2. move_to_parent_folder(path)
# # 3. display_files_and_folder(path)
# # 
# # the task is to
# # print all files of folder_3
# # print all files of folder_1

# # while calling open_folder function you can use hardcoded value for folder_name argument i.e folder_3
# # hint: use os.path.join, os.path.abspath, os.getcwd, os.listdir
# # no need to use loop