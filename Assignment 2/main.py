# 1. output the numbers from 1 to 10 using range function and for loop
# output should be like
# 1
# 2
# 3
# # etc

# for i in range(10):
#     print(i+1)


# 2. output the numbers from 35 to 50 using range function and for loop
# output should be like
# 35
# 36
# 37
# etc

# for i in range(35,51):
    # print(i)

# 3. output the numbers from -15 to -25 using range function and for loop
# output should be like
# -15
# -16
# -17
# etc

# for i in range(-15,-26,-1):
#     print(i)

# 4. output the numbers from 5 to -10 using range function and for loop
# output should be like
# 5
# 4
# 3
# etc

# for i in range(5,-11,-1):
#     print(i)

# 5. output the numbers from 0 to 50 incremented by 3 using range function and for loop
# output should be like
# 0
# 3
# 6
# 9
# etc

# for i in range(0,50,3):
#     print(i)



# 6.  Write a program to Generate Multiplication Table of 2 using range function and for loop
# output format should be like
# 2 x 1 = 2
# 2 x 2 = 4
# etc

# for i in range(0,12,2):
#     print(f"2 * {i} = {2*i}")

# 7. Write a Python program to sum all the items in a list use for loop. consider the list [3, 5, 2, 1, 4]
# output should be 15
# hint: 
# create a variable x outside the loop and assign the value 0
# inside the loop increment the value of x with the local variable of loop
# x += i

# list=[3, 5, 2, 1, 4]
# x=0
# for items in list:
#     x+=items
# print(x)

# 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]
# output should be 5
# hint:
# create a variable x outside the loop and assign the value 0
# inside the loop compare the variable x with the local variable of loop

# list=[3, 5, 2, 1, 4]
# x=0
# for i in list:
#     if x<i:
#         x=i
# print(x)

# 1. Write a Python program to multiply all the items in a list and use for loop. consider the list [3, 5, 2, 1, 4].
# output should be 360
# hint: use a variable x outside the loop and assign the first value of list
# inside the loop * the value of x with the local variable of loop
# x *= 

# list= [3, 5, 2, 1, 4]
# x=3
# for i in list:
#     x*=i
# print(x)

# 2. create a list from 0 to 100 using range function and iterate over the list
# display the number that satisfied following conditions
# The number must be divisible by 5
# If the number is greater than 30 and less than 50 then skip it
# If the number is greater than 80, then stop the loop

# for i in range(0,100):
#     if i>80:
#         break
#     elif i%5==0 and not(i>30 and i<50):
#         print(i)    


# 3. consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# display the word that contains character longer than 5
# the output should be freedeom and popcorn

# list=['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# for name in list:
#     if len(name)>5:
#         print(name)

# 4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements using for loop. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']

# list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# remove = [0, 4, 5]

# result_list = []
# for i in range(len(list)):
#     if i not in remove:
#         result_list.append(list[i])

# print(result_list)

# 5. Write a program to display odd numbers only. odd number upto 100
# hint use for loop and range function

# for i in range(1,100,2):
#     print(i)

# 6. List contains 30 elements. Display first 5 and last 5 elements

# full_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# first= full_list[:5]
# last= full_list[-5:]

# print(first)
# print(last)





# 7. Display output: helloworld from the list [‘h’, ‘e’, ‘l’, ‘l’, ‘o’, ‘w’, ‘o’, ‘r’, ‘l’, ‘d’]
# output should be 'helloworld' in one line

# list= ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
# str=''
# for item in list:
#     str+=item
# print(str)

# 8. Write a Python program to append a list to the second list.
# consider l1 is [1, 2, 3, 4, 5] and l2 is []
# using loop add items of l1 in l2

# l1 = [1, 2, 3, 4, 5]
# l2=[]
# for item in l1:
#     l2.append(item)
# print(l2)

# 9. consider the list ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
# use for loop and find the count that how many times the word "hi" present in list.
# output should be 3    


# list=['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
# count=0
# for item in list:
#     if item == "hi":
#         count+=1
# print(count)