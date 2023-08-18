# Write a Python program to copy a list using for loop. consider a list
# li = [1, 2, 3, 4]
# li_2 = []
# use for loop and add al the items in li_2

# for item in li:
#     li_2.append(item)
# print(li_2)


# Write a Python function that takes two lists and returns True if they have at least one common member.
# consider list l1 = [1, 2, 3, 4] and l2 = [5, 6, 7, 3]
# in both list value "3" is common
# use for loop
# hint: nested loop


# l1 = [1, 2, 3, 4] 
# l2 = [5, 6, 7, 3]

# for item in l1:
#     for i in l2:
#         if item == i:
#             print("Common Exist",item)


# Write a program to display index and the values (both) of a list using for loop. consider a list l = [100, 200, 300, 400]
# output: 
# 0 100
# 1 200
# 2 300
# 3 400

# l = [100, 200, 300, 400]
# l2 = [1, 2, 3, 4]
# for i in l2:
#     for j in l:
#         print(i,j)
#         break

# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# output:
# {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1, "f": 1, "g": 1, "h": 1}
# hint: use nested loop

# l1 = ['a', 'b', 'c', 'd']
# l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# l3=[]
# count=0
# for item in l1:
#     for i in l2:
#         if item == i:
#             count+=1
#     if count>0:
#         l3.append({item:count})
#         count=0
# print(l3)

# consider the number 2783, the number consists of 4 digits.
# Count the total number of digits in a number using while loop.
# instruction (hint):
# x = 2783
# counter = 0
# run while loop as long as x becomes 0
# increment the counter inside while loop
# divide x by 10 using floor division syntax "//"

# counter=0
# num=2783
# while num>0:
#     num=num//10
#     counter+=1
#     print(num,counter)
# print(counter)

# Write a program that takes user input and display it. The program keep ask user the input until user enters “0”



# def checkNum(num):
#     while num <0:
#         print("Please enter a positive number")
#         num=int(input("Enter any number: "))
#         print(num)

# num=int(input("Enter any number: "))
# checkNum(num)


# Write a program and ask user to enter number, 5 times using while loop. store each value in list.
# calculate the sum of all values in a list

# def sum(list):
#     total=0
#     for item in list:
#         total+=item
#     return total

# n=0
# list=[]
# while n<5:
#     num=int(input("Enter a number"))
#     list.append(num)
#     n+=1
# total=sum(list)
# print(total)



# Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.

# sum=0
# num=int(input("enter any number: "))
# while num>0:
#     sum+=num 
#     num=int(input("Please Enter a negative number: "))
# print(sum)

# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."

# name=input("Enter a name: ")
# while name != "END":
#     name=input("Enter a name: ")
#     name=name.upper()
#     if name == "I AM DONE":
#         print("I AM DONE")
#         break


# consider the list l1 [11, 33, 50]. use for loop to output the result like "113350"

# l1=[11, 33, 50]
# l1=''.join(str(e) for e in l1)
# print(l1)


# Write a Python program to copy a dict using for loop. consider a dict
# d1 = {"id": 1, "name": "your-name", "gender": "male"}
# d2 = {}
# # use for loop and add al the items in d2
# # hint: https://github.com/mdanish0320/teaching-class/blob/de18a6216425cde375c82a793480919af824a67c/JP-BE-PY-batch-1/loop/enumerate_.py#L12C1-L19C16


# for item in d1:
#     d2[item]=d1[item]
# print(d2)











# Write a program to create a function that takes two arguments, name and age. print them inside function.

# def userData(name,age):
#     print(name,age)

# userData("hurmat",23)


# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

# def show_employee(name,salary=9000):
#     print(name,salary)
# show_employee("hurmat",10)

# Write function that accepts different values as parameters and returns a list
# consider the below varables
# a = 4
# b = 8
# c = 10
# d = 12
# pass above values to the function and return the list
# output: [4, 8, 10, 12]

# def showList(a,b,c,d):
#     list=[]
#     list.extend([a,b,c,d])
#     return list
# myList=showList(2,4,5,7)
# print(myList)

# Write a function called km_to_miles that takes kilometers as a parameter, converts it into miles and returns the result.

# def km_to_mile(km):
#     one_mile=0.62
#     miles=km*one_mile
#     return miles
# total=km_to_mile(float(input("Enter how many km: ")))
# print(total)

# Write a function called is_divisable_by_11 that takes an integer as an parameter and returns whether it is divisible by 11 or not.

# def is_divisable_by_11(num):
#     if num%11==0:
#         return print("It is divisible by 11",)
#     else:
#         return print("Its not divisible by 11")
    
# num=int(input("Enter any number: "))
# is_divisable_by_11(num)


# Write a function called get_highest that takes 2 numbers as parameters and returns the highest of the 2 numbers.

# def get_highest(a,b):
#     if a>b:
#         return a
#     else:
#         return b
    
# num1=int(input("Enter first number"))
# num2=int(input("Enter second number"))
# highestNo=get_highest(num1,num2)
# print(highestNo)


# Write a function called fuel_cost that takes 2 numbers as parameter "distance" as required arg and "fuel_per_liter" as optional arg that has default value to 280. The function should return the cost in Rs.

# def fuel_cost(distance,fuel_per_litre=280):
#     return distance*fuel_per_litre


# total=fuel_cost(2)
# print(total)

# Write a function called is_valid_email  that takes an email address as an argument and returns True/False depending on whether it is a valid email address.

# Check rules:
# Must contain at least 1 character before the at symbol
# Must contain an @ symbol
# Must have at-least 1 character after the @ symbol and before the period(.)
# Must contain at least 1 character after the last period(.).
# Maximum 256 characters
# Must start with a letter or a number

# hint: use if statement 6 times to check each rule. if any one rule failed return false# Write a program to create a function that takes two arguments, name and age. print them inside function.


# def is_valid_email(email):
#     if len(email) > 256:
#         return False
    
#     if '.' not in email or email.index('.') < email.index('@') + 2:
#         return False
    
#     if email[-1] == '.':
#         return False
    
#     if not email[0].isalpha() and not email[0].isdigit():
#         return False
   
#     if '@' not in email or email.index('@') == 0:
#         return False

#     return True

# email=input("Enter any email: ")