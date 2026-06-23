# #  Basics – Variables, Data Types, Input/Output, Loops, Conditionals  questions 

# Q1. Write a Python program to swap two variables.

# a = int(input("enter the number :  "))

# b = int(input("enter the number :  "))

# print(a)
# print(b)

# a, b = b,a 
# print(f"the new value of a is   {a}  and the new value of b is  {b}")

# Q2. Take user input and display it back to the user.

# a = input("enter the name  :  ")


# print(f"my name is {a}")

# Q3. Write a program to check if a number is even or odd.

# num =int(input("enter the number to check that even or odd :  "))

# if num%2==0:
#     print("even number")
# else:
#     print("odd number")


# Q4. Create a program that prints the multiplication table of a given number.

# num = int(input("enter the number to print that table :  "))

# for i in range(1,11):
#     print(f" {num} * {i} = {num*i}")


# Q5. Write a program to find the largest of three numbers.

# num_1 = int(input("enter the number a : "))

# num_2 = int(input("enter the number b : "))

# num_3 = int(input("enter the number c : "))


# if num_1>  num_2 and num_1> num_3:
#     print(f"number 1 is greator {num_1}")
# elif num_2>num_3:
#     print(f"number 2 is greator {num_2}")
# else:
#     print(f"number 3 is greator {num_3}")


# Q6. Convert temperature from Celsius to Fahrenheit.

# c=int(input(" enter the temperature to conver in fahrenheit"))

# F = c * 1.8 + 32

# print(F)


# Q7. Write a program to calculate the factorial of a number using a loop.

# n = int(input("enter the number to print factorial of it "))

# factorial=1

# for i in range(1,n+1):
#     factorial*=i

# print(f" the factorial of this number {n}  is  :  {factorial}")    


# Q8. Create a program to count the number of vowels in a string.

# string= input("enter the string to find the vowels in it :  ")

# count=0
# for char in string:
#     if char in "aeiou":
#         count+=1

# print(count)


# Q9. Write a Python script to reverse a given string.


# string= input("enter the string to reverse it  :  ")

# str=""
# for i in range(len(string)-1,-1,-1):
#     str+=string[i]
#     print(string[i])


# print(str)

# print(len(string))


# Q10. Check if a number is a palindrome.

# num= int(input("enter the number of check is it palindrome or not"))

# copynum=num
# re_num=0

# while num > 0:
#     re_num=re_num*10+ num%10
#     num=num//10
# print(re_num)
# if copynum==re_num:
#     print("palindrome")
# else:
#     print("not palindrome")

# Q11. Write a program to find the sum of first N natural numbers.

# n  =int(input("enter the first n natural numbers "))

# b=0
# for i in range(1,n+1):
#     b=b+i

# print(b)

# Q12. Create a number guessing game.

# import random

# num=random.randint(1,11)



# count=0

# while True:
#     guess_num=  int(input("guess the number game so guess! : "))

#     if num==guess_num:
#         count+=1
#         print(f"win : {guess_num}  the guess number is : {num} and the tries are : {count}")
#         break
    
#     elif num < guess_num:
#         count+=1
#         print('think little lower')

#     elif num > guess_num:
#         count+=1
#         print("think little upper") 
    
#     else:
#         print("now this is correct")



# Q13. Write a program to print all prime numbers between 1 and 100.

# n= int(input("enter the range to find prime number"))

# for i in range(2,n+1):
#     is_prime= True
#     for num in range(2,int(i**0.5)+1):
#         if i%num==0:
#             is_prime= False
            
#             break
#     if is_prime:
#         print(i)



# Q14. Check if a given year is a leap year or not.

# year= int(input("enter the year to check it is leap year or not:  "))

# if year%400==0:
#     print("leap year")
# elif year%100!=0 and year%4==0:
#     print("leap year") 
# else:
#     print("not a leap year")    



# Q15. Create a program to print the Fibonacci series up to N terms.

# n = int(input("enter the number for fibonacci series :"))

# a=0
# b=1

# for i in range(n):
#     print(a)

#     c=a+b
#     a=b
#     b=c



# Q16. Write a program to find the GCD(reatest common divisor) of two numbers.

# num1=int(input("enter the first  num:   "))
# num2=int(input("enter the second num:   "))

# gcd=1

# for i in range(1,min(num1,num2)+1):
#     if num1%i==0 and num2%i==0:
#         gcd=i

# print(gcd)



# Q17. Write a program to find the LCM of two numbers.


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a > b:
#     start = a
# else:
#     start = b

# for i in range(start, a * b + 1):
#     if i % a == 0 and i % b == 0:
#         print("LCM is:", i)
#         break


# Q18. Check whether a character is a vowel or consonant.


# ch=input("write a string that character is vowel or consonants ")


# if ch in "aeiouAEIOU":
#     print("this is vowel ",)
# else:
#     print("this is consonents")    


# Q19. Write a program to calculate the sum of digits of a number.



# n = int(input("enter the number to add there digit :  "))

# sum=0
# while n>0:
#     sum+=n%10
#     n=n//10

# print(sum)    




# Q20. Create a program to find the second largest number in a list.  (done after learn list concept)


# Q21. Write a program to count the number of digits in an integer.

# n = int(input("enter the number to add there digit :  "))

# count=0

# while n>0:
#     count+=1
#     n=n//10

# print(count)


# Q22. Create a program to print all Armstrong numbers between 1 to 1000.

# n =int(input("enter the number to print all armstring number :  "))

# for i in range (1,n+1):

#     original = i 
#     temp=i    
#     total = 0

#     while temp>0:
#         digit= temp%10
#         total+=digit**3
#         temp//=10

#     if total == original:
#         print(original)




# Q23. Write a Python program to print a pattern of stars in a triangle.

# n="*"

# for i in range(1,6):
#     print("*" * i)


# Q24. Create a calculator app using if-else.

# number1=int(input("enter the first number :  "))
# number2=int(input("enter the second number :  "))

# choose=input("choose from this (+,-,*,/) :  ")


# if choose == "*":
#     print(f"multiplication of these number is :{number1*number2}")
    
# elif choose == "+":
#     print(f"addition of these number is :{number1+number2}")

# elif choose == "-":
#     print(f"subtraction of these number is :{number1-number2}")
# elif choose == "/":
#     print(f"divide of these number is :{number1/number2}")
# else:
#     print("wrong operator")



# Q25. Write a program to display the ASCII value of a character.

# single_char = input("Enter a character: ")

# print(f"ascii value of this character is : {ord(single_char)}")


# Q26. Convert a decimal number to binary using loops.

# n = int(input("Enter a decimal number: "))

# bi=""

# while n>0:
#     bi=str(n%2)+bi
#     n=n//2


# print(f"binary of this number is {bi}")


# Q27. Create a program to find the square root of a number.

# num=int(input("enter the number to find square root : "))

# for i in range(1,num+1):
#     if i*i==num:
#         print(F"the square root is  {i} ")
        
# else:
#     print("entered number have not perfect square root ")





# Q28. Write a program to find the sum of all even numbers in a list.

# do when completion of list topic



# Q29. Create a program to check whether a number is prime or not.


# num=int(input("enter the number to check either prime or not : "))

# if num<=1:
#     print("not prime")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime number")


# Q30. Write a program to display the cube of the number up to an integer.


# n=int(input("enter the number to find cube  :  "))

# for i in range(1,n+1):
#     print(f"{i} cube root is : {i**3}")