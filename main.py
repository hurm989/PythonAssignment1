# Write a program to check whether a person is eligible to vote or not?

# age=int(input('Enter Your Age: '+ "\n"))
# if age>18:
#     print(f"You are {age}, eligible to vote")
# else:
#     print(f"You are {age}, not eligible to vote")


# Write a program to check char is vowel or not.
# char=input("Plase enter any charcter: " + "\n")
# if(char == "a" or char=='e' or char == "i" or char == "o" or char == "u"):
#     print("Its a vowel")
# else:
#     print("Its a consonant")


# Write a program to check the number is positive or negative. User input.
# num=float(input("Enter any number: "))
# if num > 0:
#     print("Positive Number")
# else:
#     print("Negative Number")


# Write a program to check whether a number is odd or even?
# num=int(input("Enter any number: "))
# if num%2==0:
#     print("Even Number")
# else:
#     print("Odd Number")


# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100
# num=int(input("Enter your course marks"))
# if num>=91 and num<=100:
#     print("Grade A1")
# elif num>=81 and num<91:
#     print("Grade A")
# elif num>=71 and num<81:
#     print("Grade B")
# elif num>=61 and num<71:
#     print("Grade C")
# elif num>=51 and num<61:
#     print("Grade D")
# elif num>=41 and num<51:
#     print("Grade E")
# elif num>=33 and num<41:
#     print("Grade F")
# else:
#     print("Invalid")



# Write a program to check whether a number is divisible by 7
# num=int(input("Enter any number: "))
# if num%7==0:
#     print("this number is divisible by 7")
# else:
    # print("Not divisib by 7")


# Write a program to check if year is leap year.
# NOTE: search on google of what leap year is.
# year=int(input("Enter any year: "))
# if year%4==0:
#     print("Leap Year")
# else:
#     print("Not a leap year")


# Write a program to ask user its name and check whether name consists of 5 or more letters
# name=input("Enter name: ")
# lengthName=len(name)
# if lengthName<5:
#     print("Name consist of less than 5 letters")
# elif lengthName>5:
#     print("Name consist of greater than 5 letters")
# elif lengthName==5:
#     print("Name consist of 5 letters")
# else:
#     print("Invalid")


# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator. Perform operation accordingly
# for example
# input1 is 5 and input2 is 10 and input3 is +
# then output should be 15
# input1 is 5 and input2 is 10 and input3 is *
# then output should be 50


# num1=float(input("Enter any number: "))
# num2=float(input("Enter any number: "))
# operator=input("Enter any operator: ")
# if operator=="+":
#     print(f"Addition is {num1+num2}")
# elif operator =="-":
#      print(f"Subtraction is {num1-num2}")
# elif operator =="*":
#      print(f"Multiplication is {num1*num2}")
# elif operator =="/":
#     print(f"Division is {num1/num2}")
# else:
#      print("Invalid Input")



# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.

# for example
# input1 is 10
# output should be "10 is only divisible by 2"

# input1 is 9
# output should be "9 is only divisible by 3"

# input1 is 12
# output should be "12 is divisible by 2 and 3"

# num=int(input("Enter any number: "))
# if num%2==0 and num%3==0:
#     print(f"Number is divisible by 2 and 3")
# elif num%2==0:
#     print(f"Number is divisible by 2")
# elif num%3==0:
#     print(f"Number is divisible by 3")
# else:
#     print("Invalid input")

# Write a program that accepts 2 inputs from user and check which number is largest.

# for example:
# input1 is 5 and input2 is 10
# output should be 10 as this number is larger than 5

# num1=int(input("Enter any number: "))
# num2=int(input("Enter any number: "))
# if num1>num2:
#     print(f"{num1} is grater than {num2}")
# elif num1<num2:
#     print(f"{num2} is grater than {num1}")
# elif num1==num2:
#     print(f"{num1} is equal to {num2}")
# else:
#     print("Invalid")




# Write a program that accepts 3 input from user and check which number is largest.

# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 15 as this number is larger than 5 and 10

# num1=int(input("Enter any number"))
# num2=int(input("Enter any number"))
# num3=int(input("Enter any number"))
# large = 0
# if num1 > num2 and num1 > num3:
#     large = num1
# if num2 > num1 and num2 > num3:
#     large = num2
# if num3 > num1 and num3 > num2:
#     large = num3
# print(large, "is the largest of three numbers.")


# Write a program that accepts 3 input from user and check the second is largest.

# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 10 as this number is larger than 5 and smaller than 15


# a=int(input("Enter any number"))
# b=int(input("Enter any number"))
# c=int(input("Enter any number"))
# large = 0
# if (a < b < c) or (c < b < a):
#     print(b,"is between num1 and 2")
# elif (b < a < c) or (c < a < b):
#     print(a,"is between num1 and 2")
# else:
#     print(c,"is between num1 and 2")


# Write a python program that accept user an input. The valid input should be of following
# - GREEN or gREEN or green etc 
# - RED or red or rEd etc 
# - YELLOW or yellow or yELlOw etc

# program should display the following message on checking above input
# Car is allowed to go
# Car has to wait
# Car has to stop
# invalid input
# light=input("Enter any light: ")
# if light=="GREEN" or light == "gREEN" or light=="green":
#     print("Car is allowed to go")
# elif light=="RED" or light == "red" or light=="rEd":
#     print("Car has to stop")
# elif light=="YELLOW" or light == "yellow" or light=="yELlOw":
#     print("Car has to wait")
# else:
#     print("Invalid")

# Write a program to trace your subject mark. Your program should fulfill the following conditions:

# If the subject mark is below 0 and above 100, print “error: mark should be between 0 and 100 only”
# display "you are fail" if their mark is below 50.
# display "you are pass" if they score 50 and above.
# If subject mark is between 50 and 60, Remark: Good
# If subject mark is between 60 and 80, Remark: Very Good
# If subject mark is between 80 and 100, Remark: Outstanding

# for example
# input1 is 70
# output should following

# you are pass
# Remark: Very Good

# for example
# input1 is 90
# output should following

# you are pass
# Remark: Outstanding


# for example
# input1 is 49
# output should following

# you are fail

# marks=int(input("Enter your marks: "))
# if marks>100 and marks<0:
#     print("Error")
# elif marks<50:
#     print("You are fail")
# elif marks>50:
#     print("You are pass")
#     if marks>80 and marks<100:
#         print("Outstanding")
#     elif marks>60 and marks<80:
#         print("Very Good")
#     elif marks>50 and marks<60:
#         print("Good")

# Create a list of juices, add 5 items using append
# list=[]
# list.append("Apple Juice")
# list.append("Mango Shake")
# list.append("Orange Juice")
# list.append("Pineapple Juice")
# list.append("Banana Shake")
# print(list)


# Create a list of cars, add 5 items using insert
# list=[]
# list.insert(0,"corolla")
# list.insert(1,"mehran")
# list.insert(2,"cultua")
# list.insert(3,"alto")
# list.insert(4,"revo")
# print(list)

# Remove last item from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’]	using pop and len 
# list=["bed", "table", "chair", "sofa"]
# list.pop()
# print(list)


# output should display [‘bed’, ‘table’, ‘chair’]

# Remove second last item from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’] by len and index
# list=["bed", "table", "chair", "sofa"]
# list.pop(len(list)-2)
# print(list)


# output should display [‘bed’, ‘table’, ‘sofa’]

# Remove first item from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’]
# list=["bed", "table", "chair", "sofa"]
# list.pop(0)
# print(list)

# output should display [‘table’, ‘chair’, ‘sofa’]

# Remove the item “chair” from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’]
# list=["bed", "table", "chair", "sofa", "chair"]
# list.remove("chair")
# print(list)

# output should display [‘bed’, ‘table’, ‘sofa’]

# Remove all “chair” from the list [‘bed’, ‘table’, ‘chair’, ‘sofa’, ‘chair’]

# output should display [‘bed’, ‘table’, ‘sofa’]

# list=["bed", "table", "chair", "sofa", "chair"]
# for x in list:
#     if x=="chair":
#         list.remove(x)
# print(list)



# Merge two lists [‘A’, “B”, “C”] and [“D”, “E”, “F”]

# output should display [‘A’, “B”, “C”, “D”, “E”, “F”]

# list=["A","B","C"]
# list2=["D","E","F"]
# list3=list+list2
# print(list3)

# Write a Python program to check if a list is empty or not.
# list = []

# if len(list):
#     print("list is not empty")
# else:
#     print("list is empty")
