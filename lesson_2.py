# --------------------FUNCTIONS----------------------

# Functions in Python group reusable code into a block that
# can be executed by calling the function name. 
# This helps avoid repetition and makes programs modular and readable.

# There are many in-build functions in python like print(), input(), len() etc.
 

# you can create your own function and they are called as user defined functions. 
# To make your own function you have to use def keyword and then name the function.
# After this you have to call the function using name() and paranthesis.

# def hello(a,b):
#     print(f"the sum of a and b is {a+b}")

# hello(23,3)

# def hello(name,age):
#     print(f"your name is {name} and your age is {age}")

# hello(age = 23,name = "Tushar")


# def palindrome(n):

#     rev=""

#     for i in range(len(n)-1,-1,-1):
#         rev=rev+n[i]

#     if rev==n:

#         print("pallindrome")
#     else:
#         print("not a palinrome")

# palindrome("naman")                
# palindrome("school")

# def hello(a):           ------ # parameters
#     return("hello , welcome to our world ", a)


# print(hello("Tushar"))   -----#arguments 



# DATA STRUCTURES in python

# in python we have 4 types of in-build data structure
# List, Tuple, Dictionary, Set.


#------------------------- LIST---------------------------

# Before starting we need to understand some of the terminology.
# Mutability refers to whether an object's value can be changed after creation. And List allows this 
# we know data structures are used to store multiple values so duplicates means same value occuring multiple time. List allows this List maintains ordered data structure maintains the sequence of elements as they were inserted. This means you can access elements using their position(index)
# List have heterogenous nature that means we can have multiple data types inside the list.

# lis=[12,23,34,56,76,]

# print(lis[3])

# lis[1]= 99

# print(lis)


#  Loops on list

# stlist= [23,45,234,76,97,"dfg", -343, 45]

# for i in range(len(stlist)):
#     print(stlist[i])










# now see some of the method of lists 

# num= [5,2,9,1,5,6]   making list 

# num.append(10)  add 10 at the end
# num.insert(2, 15) inserts 15 at index 2
# num.extend([20,25,30]) add multiple elements at the end 
# num.remove(5)  Removes the first occurrence of 5
# popped_item= num.pop(3) removes and stores the element at index 3
# index = num.index(6)  find the index of 6
# count_5= num.count(5) counts occurences of 5
# num.sort() sorts the list in ascending of 5
# num.reverse()  reverses the list order
# new_numbers = num.copy()  creates a copy of the list
# num.clear() removes all elements from the list

