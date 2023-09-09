# create a text file and add the below content without quotation marsk
# """
# Hi *user*!

# We've found the best article for you based on your interest: *title*
# Please click *here* to open the article
# """

# task is to read the above file and update the placeholder i.e *user*, *title* and *here*
# and store the updated content in user_email.txt
# run program three times with different name, title and link

# after running the program three times
# the file user_email.txt must have all three users content



# def _change_content(name,title,here): 
#     file=open("file.txt","r")
#     fileContent=file.read()   
#     fileContent=fileContent.replace("*user*",name)
#     fileContent=fileContent.replace("*title*",title)
#     fileContent=fileContent.replace("*here*",here)
#     userEmail=open("useremail.txt","a")
#     userEmail.write(fileContent+'\n')

# _change_content('hurmat','abc','xyz')
# _change_content('hurmatNaz','sports','www.sports.com')
# _change_content('hur','game','www.games.com')