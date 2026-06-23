# # Download python.org
# # vscode (IDE = Integrated development evironment)
# # extensions python , code runner

# # -----lets start learning python.-----

# # --->>>>Basics– Variables, Data Types, Input/Output, Loops, Conditionals

# # ---Comments in python--- 
# # comments are ignored by python interpreter.
# # use (#)  to writing a comment in python.
# """ this is multiline comment are absent in python but we use docstring
#  """

# ---------------------important thing most of people cannot understand is :


# ----Square brackets---- []----  = indexing or slicing (sequence access): n[i], n[1:4].
# -----Parentheses----- () ----  = function call or grouping: f(x), (a + b).
# --------Curly braces ----{} -----  = sets or dict literals and format placeholders.

# # ---variable in python---

# # making storage to store thing or naming the container

# # eg. 
#             # container= "bharat"
#             # year= 2026

# # cannot use number at variable name start.
# # no space, no special character only underscore.

# # name conventions
# # write variable in python using 3 ways 
# # firstSchool - camel case 
# # FirstSchool - pascal case
# # first_school - snake case


# # Datatype in python

# # the types of data that stored in python and that defines the datatype of variables are
# # In python has built in data types for different kinds of data .

# # number - integer, float(decimal), complex.


# # natural number= 1,2,3,4,5,,.....infinite.
# # whole number= 0,1,2,3,4,5.....infinite.
# # integer number= infinite......-5,-4,-3,-2,-1,0,1,2,3,4,5.......infinite

# a= 23

# print(type(a))

# # float number= 12.3,  23.5,   12/3 (p by q is float - 4.0)

# b= 3.4 

# print(type(b)
#       )
# # complete=  in maths there is a imaginary value called iota (j) 

# c= 45j

# print(type(c))


# # -----strings - store anything basically it is text used between "" and '' to store both work same

# st= "asdfgkhj !@#@#$% 123415"

# print(type(st))

# # Boolean - theres nothing much to say this is the data type which will and always give result of True and False
# #  T of True and F of False is always capital

# g= True
# h= False
# print(type(g),type(h))


# # String takes extra space because every character have unicode.
# # example to write letter usning unicode

# t = 69
# print(chr(t))

# # ---String indexing

# ind= "this is python journey"             
# #  indexing start from 0  and in negative indexing start from -1

# print(ind[-2])

# # ---string slicing 

# # a[ start : stop : end]

# print(ind[0:4:1])


# # Type conversions :

# # string in
# a = 12 
# a= str(a)
# print(type(a))

# # int

# b= "12"
# b= int(b)
# print(type(b))

# # boolean
# c = "tushang"
# print(bool(a))


# # there are 7 value that are falsy value 
# # False
# # 0
# # 0.0
# # ""
# # []
# # ()
# # {}


# # type convertion 2 types 
# #-------- 1 inplicit 
# a=12 
# print(a/2)

# # output is 6.0 it automatically convert in float result

# # -------- 2 explicit

# # this is already have example like int convert in string and string num convert in int and boolean true false

# # now we are learning about input output in python 

# # syntax of taking input from user in python is 

# a= int(input("enter the age  "))  # default it take data type is string so if like user need integer so write and mention a data type

# print(a)
# print(type(a))

# # PQ are 
# # accept number from a user.
# # accept age from the user and print it.
# num=int(input("enter the number"))

# name = input ("enter the nmae ")
# age= int(input("enter your age "))
# # print("my age is  ",age)                   


# # in output there is a formated string 

# print(f"hello my name is {name}, my age is {age}")

# # ---------operators----------

# # Operators are symbols that perform operations on variables
# # and values. Python has several types of operators for
# # different tasks like arithmetic, comparison, logical operations,
# # and more

# # <<<<<---arithmetic operator

# # Arithmetic operators perform mathematical operations like
# # addition, subtraction, multiplication, division, etc

# #  There are 7 types of arithmetic operator.G


# num_1 =float(input("enter the first number : "))
# num_2 =float(input("enter the second number: "))
# #  addition 
# print(f"the addition is {num_1+ num_2}")

# #  subtraction 

# print(f"the subtraction is {num_1 - num_2}")

# #  multiplication 

# print(f"the multiplication is {num_1 * num_2}")

# #  division 

# print(f"the division is {num_1 / num_2}")

# #  Floor division 

# print(f"the floor division is {num_1 // num_2}")

# #  modulus 

# print(f"the modulus(ramainder) is {num_1 % num_2}")

# #  Exponentiation 

# print(f"the exponentiation(how many multiply times) is {num_1 ** num_2}")


# # ------------------Assignment operator 

# # Assignment operators are used to assign values to variables.
# # Python also provides compound assignment operators that
# # perform operations like addition, subtraction, multiplication,
# # etc
# #  A basic assignment operator is simple =.

# # a= 34   this is assigning the value basically store in variable 

# # ----------Compound assignment operator------------

# # Compound assignment operator combines arithmetic
# # operations with assignment

# # reassign value 
# a = 20

# a= a+45

# # print(a)
# # Using compound assignment operators the reassigning
# # works better

# #  += Add and assig
# #  -= Subtract and assig
# #  *= Multiply and assign
# #  /= Divide and assig
# #  //= Floor divide and assig
# #  %= modulus and assig
# #  **= Exponentiation and assign


# # ------------Comparison operator----------

# # Comparison operators, also called relational operators, are
# # used to compare two values
# #  Comparison operators will always provide Boolean result that
# # is True and False
# #  comparison operators are as follow


# a= int(input("enter the number"))
# b= int(input("enter the number"))

# # !!!$$$@@@ important : to find out the ascii value in python write print(ord("a"))
# print(ord("A"))
# print(ord("B"))
# print("A"> "B")

# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)



# #  ==       -        Equal to
# #  !=       -        Not Equal to
# #  >        -        Greater than
# #  <        -        Less than 
# #  >=       -        Greater than or equal to 
# #  <=       -        Less than or equal to

# # Comparison operators will work with numbers but you can
# # use them with strings as well.
# # Strings will be comparing the Ascii values of string.

# # Logical operators

# # and - Return True if both condition are Tru\
# # or - Return True if at least one condition is True
# # not - Reverse the boolean value

# print(12==12 and 12> 23 and 12 < 11)  # and

# print(12==12 or 23==22 or 34>23)    #or

# print(not 19<12) # not 


# #Trivial Questions
# # Answer True and False

# # Print (126 > 13) -------> false
# # print((456 == 456) != (235 == 236) ----> true
# # print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)------> true
# # print(True and bool(0)) ------>  false


# # ------------------Conditional statement ---------

# # Conditional statements in Python allow decision-making by
# # executing different blocks of code based on conditions

# # type of conditional statement 
# # Generally there are 3 types of variation in conditional statements

# # if - Executes if the condition is True

# a = 12
  
# if a > 10:
#     print(" a is greator")
   
# # if-else - Executes if True, another if False


# a = 12
  
# if a > 10:
#     print(" a is greator")
# else:
#     print("a is not greator") 

# # if-elif-else - Checks multiple condition in sequence.


# money = int(input("enter the money you get : "))


# if money == 10:
#     print("choco bar")
# elif money == 20:
#     print("i will have a mango dolly")
# elif money ==40:
#     print("i will buy sandwich")    
# else:
#     print(" i will have a cone ")        

# # some quesions for this 

# # @ The Great thing is you can use logical operators as well.

# # Q1. Accept two numbers and print the greatest between them.

# num_1= int(input("enter the number first :  "))
# num_2= int(input("enter the number second :  "))

# if num_1 > num_2:
#     print(" number 1 is greator")
# else:
#     print(" number 2 is greator")

# # Q2. Accept the gender from the user as char and print the
# # respective greeting message
# # Ex - Good Morning Sir (on the basis of gender)

# gender= input("enter your gender male or female :   ")

# if gender == "male":
#     print(" good morning sir")

# elif gender == "female":
#     print(" good morning ma'am")

# else:
#     print(" wrong  or undefined gender")



# # Q3. Accept an integer and check whether it is an even number
# # or odd.

# num= int(input("enter the number is even or odd:   "))

# if num%2==0:
#     print("even number")
# else:
#     print("odd number")    



# # Q4. Accept name and age from the user. Check if the user is a
# # valid voter or not.
# # Ex- “hello shery you are a valid voter”

# name = input("enter you name:   ")
# age =int(input("enter your age:   "))

# if age>=18 :
#     print(f"hello {name} your age is {age}  you are eligible give vote")
# else:
#     print(f"hello {name} your age is {age}  you are not eligible to give vote")    


# # Q5. Accept a year and check if it a leap year or not (google to
# # find out what is a leap year)



# year=int(input("enter the year to check it is leap year or not:   "))

# if year%100==0 and year%400==0:
#     print(" this is leap year")

# elif year%100!=0 and year % 4 ==0:
#     print(" this is leap year")

# else:
#     print(" this is normal year")    



# # If- elif ladder

# temp=int(input("enter the temperature:  "))

# if temp < 0:
#     print(" freezing cold")

# elif 0 <= temp <=10:
#     print(" very cold")

# elif 10< temp <=20:
#     print("  cold ")

# elif 20< temp <=30:
#     print("pleasant")

# elif 30 < temp <=40:
#     print("hot")

# elif 40< temp  <=50:
#     print("very hot ")        

# else:
#     print("danger")    

# # --------------Loops in python ---------------

# # Loops in Python allow us to execute a block of code multiple times without rewriting it

# # Manually printing will take 100 code lines to print it. but using
# # loops we need only 2 lines to print 100 times, thats the power of loops.

# # there are 2 types loops in python

# # for loop 
# # while loop 

# # now first understand the range function 

# # range(start, stop , step)

# # range function use in for loops 
 
# for i in range(1,22,1):
#     print("hello tushar  ", i)

#     # reverse order in for loop 


# for i in range(20,0,-1):
#     print(i)

# # for loop on strings 

# a = " this is my python journey "
# print(len(a))

# for i in range(len(a)):
#     print(a[i])



# ste = " i am cool"

# for i in ste:
#     print(i)


# # before go on the while loop 

# # --------- learn break and continue and else---

# # ------ break-------


# for i in range(21):
#     if i == 5:
#         break
#     else:               # so the break basically stop the loop at that point 
#         print(i)


# # -----continue---------

# for i in range(21):
#     if i == 5:
#         continue
#     else:               # so the continue basically  skip that one cycle  in the loop.
#         print(i)

# # ------------else-------

# #  else works with break

# for i in range(21):
#     if i == 87:
#         print("break statement is exevuted")
#         break
#     print(i)
    
# else:
#     print("break statement is not executed")    

# # -----some question on for loop---------- 

# # -- accept an integer and print hello world n times 

# n=int(input("enter the number  : "))

# for i in range (n):
#     print("hello world")

# # print natural number up to n 

# natural= int(input("enter the number to print natural number"))

# for i in range (1,natural+1):
#     print(i)


# # reverse for loop. print n to 1

# n= int(input("enter the number :  "))

# for i in range (n,0,-1):
#     print(i)

# # take a number as input and print its table

# table= int(input("enter the table number"))

# for i in range(1,11):
#     print(f"{table}  *  {i}  =  {table*i}")


# # sum up to n terms 

# n = int(input("enter the number :  "))

# sum=0

# for i in range (n+1):
#     sum+=i

# print(sum)    

# # factorial of a number.  (means 5= 1*2*3*4*5)

# n = int(input("enter the number :  "))

# factorial=1

# for i in range (1,n+1):
#     factorial*=i

# print(factorial) 

# # print the sum of all even & odd numbers in a range separately

# n = int(input(" enter the number : "))

# even= 0
# odd = 0

# for i in range(1,n+1):
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i

# print(f"the sum of even no {even} and odd no is  {odd}")


# # print all the factor of a number. (number that divicible and give remainder 0  )

# n = int(input(" enter the number for which you want factors:  "))

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)


# # accept a number and check if it a perfect number or not. A number shose sum of factors is equal to the number itself.
# # eg:  6= 1,2,3 = 6

# n = int(input("enter the number that is perfect or not : "))

# sum=0


# for i in range (1,n):
#     if n%i==0:
#         sum+=i

# if sum ==n:
#     print("your number is perfect")
# else:
#     print("your number is not perfect")

# # check weather the number is prime or not 

# # hint : prime means either divicible by self or 1 only

# n = int(input("check wether number is prime or not "))

# count=0 
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1

# if count==2:
#     print("number is prime ")
# else:
#     print("number is not prime ")    

# # reverse a string without using in build function

# sr=input("enter the string to reverse  :   ")

# sr_= ""
# for i in range(len(sr)-1,-1,-1):
#     sr_+=sr[i]
# print(sr_)


# # check string a palindrome or not


# sr=input("enter the number to chech palindrome or not   :   ")

# sr_= ""
# for i in range(len(sr)-1,-1,-1):
#     sr_+=sr[i]

# if sr_==sr:
#     print("palindrome")
# else:
#     print("not a palindrome")    

# #  count all letters, digits and special symbols from a given string

# # given: str1 ="P@#yn26at^&i5ve"
# # expected outcome:

# # Total counts of chars, digits and symbols 

# # chars   = 8
# # digit   = 3
# # symbols = 4

# # hint: ****************************IMP*******string methods are important

# stro= "P@#yn26at^&i5ve"

# char= 0
# digit= 0
# symbol=0

# for i in stro:
#     if i.isdigit():
#         digit+=1
#     elif i.isalpha():
#         char+=1
#     else:
#         symbol+=1


# print(f" digits are : {digit}\n your chars are : {char}\n your symbols are :  {symbol}")



# #  now finally while loop  

# # ---------------WHILE loop ----------------------------

# # The while loop repeats a block of code as long as a condition
# # is True. It is useful when the number of iterations is unknown
# # before execution

# # So there is not much that you have to understand about
# # while loop it also have break, continue and else.


# a =1 

# while a<=30:
#     print(a)
#     a+=1


# # ----------------------- while  loop questions:----

# # separate each digit  of  number and print it on the new line.

# a= 678

# while a>0:
#     print(a%10)
#     a=a//10




# # accept a number print its reverse.



# a= 678
# b= 0
# while a>0:
#     b= b*10+a%10
#     a=a//10
# print(b)

# #  accept a number and check if it is a pallindromic number(if number and its reverse are equal)


# a= int(input("enter the num to check palindrome or not "))
# copy=a
# b= 0
# while a>0:
#     b= b*10+a%10
#     a=a//10

# if copy== b:
#     print("palindrome number")

# else:
#     print("not pamlindrome")    


# # create a random number guessing game with python

# import random

# num = random.randint(1,10)

# count = 0

# while True:
#     guess = int(input("enter the guess number bet 1,  10  :  "))


#     if num==guess:
#         count+=1
#         print(f"correct  you are right  your tries are {count}")
#         break
#     elif num<guess:
#         print("go little lower")
#         count+=1
    
#     elif num> guess:
#         print("go little upper")
#         count+=1
#     else:
#         print("you are in correct ")
#         count+=1


# print(f" guess num is {guess} ,  ramdom number is {num} and the tries are {count}")            



