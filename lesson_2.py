


"""-------------------------------------Functions, Lists, Tuples, Dictionaries, Sets  with comprehension -------------------------"""





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

# num= [5,2,9,1,5,6,3,4,8]  # making list 

# num.append(10)   # add 10 at the end

# print(num)

# num.insert(2, 15) #inserts 15 at index 2

# print(num)

# num.extend([20,25,30]) # add multiple elements at the end 

# print(num)

# num.remove(5)  # Removes the first occurrence of 5

# print(num)
 
# popped_item= num.pop(3)  # removes and stores the element at index 3

# print(num)

# index = num.index(6)  # find the index of 6

# print(index)

# count_5= num.count(5)  # counts occurences of 5

# print(count_5)

# num.sort()  # sorts the list in ascending of 5

# print(num)

# num.reverse()  # reverses the list order

# print(num)

# new_numbers = num.copy()  # creates a copy of the list
# print(num)
# print(new_numbers)

# num.clear() # removes all elements from the list

# print(num)



# Some question on list 


#  Print positive and negative elements of an List?

# list1=[12,23,-98,56,87,-49,-34,34]


# print("print the positive numbers: ")

# for i in list1:
#     if i >=0:
#         print(i)

# print(" print the negative number :")

# for i in list1:
#     if i <0:
#         print(i)



#   Mean of List elements?

# mean=[23,12,45,675,34,23]

# sum=0
# for i in mean:
#     sum = sum +i

# print(f"the of this list is :   {sum/len(mean)}")



#  Find the greatest element and print its index too?


# list=[23,435,11,22,67,54,875,45,45,45,45,332,75,888]

# largest=list[0]
# index= 0


# for i in range(len(list)):
#     if list[i] >largest:
#         largest=list[i]
#         index=i


# print(f"the largest number is {largest} and the indes of this number is {index}")



#  Find the second greatest element?


# list=[23,435,11,22,67,54,875,45,45,45,45,332,75,888,878]

# largest=list[0]
# sec_largest=list[0]

# for i in list:
#     if i> largest:
#         sec_largest=largest
#         largest=i
#     elif i> sec_largest:
#         sec_largest=i

# print(f"the largest number is {largest} and the second largest num is {sec_largest}")




#  Check if List is sorted or not.


# list= [12,13,14,15,16,45]


# for i in range(len(list)-1):
#     if list[i] < list[i+1]:
#         continue
#     else:
#         print("list is not sorted")
#         break
# else:
#     print("list is sorted")


#------------ list comprehension -----------------

# result = []

# for item in data:                               # normal loop 
#     if condition:
#         result.append(expression)



# result = [expression for item in data if condition]         # list comprehension
# print (result)



# =-----------------Tuple-----------------=


# Before starting we need to understand some of the terminology.

# - Tuples are not mutable, you cannot change the values of tuple
# - You can have duplicate values in tuple there are no restriction
# - tuple are ordered and you can access them through index values
# - tuple also have heterogenous nature and can have different types of data structure in tuple.

# traversed in mannerl like list
# a= (1,2,5,5,53,4,3,3,3,5,7,6,9)
 
# print(type(a))
# for i in a:
#     print(i)
# print("next\n\n\n")


# for i in range(len(a))   :
#     print(a[i]) 

# index= a.index(9)
# print(index)

# count5=a.count(5)
# print(count5)


# # tuple unpacking

# a,b,c,d=(1,2,4,5)

# print(a)
# print(b)
# print(c)
# print(d)

# print(type(a))



# a=(2,)        to make tuple with single  value insert coma with data

# print(type(a))





# ------------------------------SETS-----------------------

# Before starting we need to understand some of the terminology.

# - Sets are mutable you can change the values of set.
# - You cannot have any duplicate values in set that means every element will be unique
# - Sets are unordered and you cannot access them through index valuesO
# - Set is semi-heterogenous it can store some data types like string, numbers, tuples but not everything


# s= {3,2,5,"hello",7,4}

# print(type(s))

# b=hash((1,2,4))


# print(b)

# for i in s:   #not a fix indexing value 
#     print(i)

# ----------------sets methods-------------


# s={1,4,5,6,7}


# s.add(99)  #adds an element to the set

# print(s)

# s.remove(4) # removes 4 (raises an error if not found)

# print(s)

# s.discard(5) # removes 5 (no error if not found)

# print(s)

# popped_element = s.pop() # removes a random element

# print(s)

# s.clear() # removes all elements

# print(s)

# #-----some method to perform operation between two sets ---

# a= {1,2,3,4,5,6}
# b= {4,5,6,7,8,9}


# # ---------union
# s=a.union(b)
# s=a|b


# -----------intersection

# s=a.intersection(b)  #gives the common values in it 
# s=a&b

# -----------difference

# s= a.difference(b)
# t= b.difference(a)
# s=a-b
# t=b-a


# ---------symmetric_difference
# s=a.symmetric_difference(b)
# t=b.symmetric_difference(a) #ites remove the common values

# s=a^b
# t=b^a
# print(s)
# print(t)


# --------set comprehension------

# numbers = [1,2,2,3,3,4]



# unique = set()
# for i in numbers:                #normal 
#     unique.add(i)




# unique = {i for i in numbers}            comprehension

# print(unique)


# # ------------------------------dictionary--------------------------------------

# # Before starting we need to understand some of the terminology.

# # - Dictionaries are mutable, meaning you can  change, add, or remove key-value pairs after creation
# # - Keys must be unique, but you can have duplicates in valuesY
# # - Dictionary follows insertion order
# # – A dictionary can store different types of keys and values, like integers, strings, lists, or even another dictionary.


# d= {"name" : "rohan",
#     "age":12, "fees":15000}

# print(d["name"])

# d["name"] = "tushar"   # updating

# print(d)


# d.update({"weight" : 75}) #creating




# d["father"]= "prabhas"   # creating

# print(d)

# del d["father"]   #deleting


# print(d)

# loop on dictionary

# d= {"name" : "rohan",
#     "age":12, "fees":15000}


# for i in d:
#     print(i)

# for i in d.values():
#     print(i)    

# # ----------some methods of dictionary ---------

# # d.clear()

# # print(d)

# # lets discuss about the shallow copy and deep copy 

# # b=d            #this is the deep copy  and in this the name value will change 

# # b["name"] = "yuvi"

# # print(d)


# b=d.copy()         #this is the shallow copy  and in this the original dist will not change because using .copy()  function   


# b["name"] = "yuvi"
# print(d)


# d2= d.get("name")             # to the value of key 
# print(d2)

# d2=d.items()
# print(d2)



#  ---------------Dictionary comprehension---------

# square = {}
# for i in range(1,6):
#     square[i] = i*i                    # normal way

# print(square)

# in comprehension way--

# square = {i: i*i for i in range(1,6)}

# print(square)


# --now some questions on dictionary---

# # Write a Python script to merge two Python dictionaries?

# d={10:100,20:200,30:300,40:400,50:500}
# d2={60:600,70:700,80:800,90:900}

# for i in d2:
#     d[i]=d2[i]

# print(d)


# # Write a Python program to sum all the values in a dictionary?

# d={10:100,20:200,30:300,40:400,50:500}

# sum=0

# for i in d:
#     sum+=d[i]

# print(f"the sum of all value present in dictionary d :  {sum}")
# Count the frequency of each element of list and store in dictionary 

# l=[1,1,1,1,1,2,2,2,2,2,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,8,8,9,9,9,9,9]

# dl={}

# for i in l:
#     if i in dl.keys():
#         dl[i]+=1
#     else:
#         dl[i]=1             # here dl[i] is the value of key that like 1:1 then 2:1

# print(dl)



# Write a Python program to combine two dictionary by adding values for common keys.

# d={10:100,20:200,30:300,40:400,60:500}
# d2={60:600,70:700,80:800,40:900}

# for i in d2:
#     if i in d:
#         d[i]+=d2[i]
#     else:
#         d[i]=d2[i]


# print(d)
