""" Topic: filehandling, Exception / error handling, module,
 or left topic of list is list comprehension """



# Q1. Write a Python script to read a file and print its contents.



# with open("lesson_1.py", "r", encoding="utf-8") as p:
#     print(p.read())


# Q2. Create a file and write your name into it.


# with open("over.txt", "w") as w:
#     w.write("this is overwrite")

# Q3. Handle a ZeroDivisionError using try-except.

# try:
#     a=10
#     b=0

#     print(a/b)
# except ZeroDivisionError:
#     print("cannot divide by zero ")


# Q4. Write a program to handle file not found error.

# try:

#     with open("hello.txt", "r") as r:
#         print(r.read())

# except FileNotFoundError:
#     print("entered file not exist")        


# Q5. Create a module with a function and import it in another file.

# import addition

# a=10
# b=24

# print(addition.add(a,b))

# Q6. Use a list comprehension to filter even numbers from a list.

# num = [1,2,3,4,5,6,7,8,9,10,11]

# filter_even= [i for i in num if i%2==0]

# print(filter_even)


# Q7. Write a generator that yields even numbers up to N.


# def even(num):

#     for i in range(1,num+1):
#         if i%2==0:
#             yield i


# for number in even(10):
#     print(number)

# Q8. Create a program to count lines and words in a file.

# with open("add.txt", "r") as file:
#     lines=file.readlines()
# print(lines)  # readlines() converts the lines into a list.

# count_lines=len(lines)
# print(count_lines)

# count_words=0
# for line in lines:
#     count_words+=len(line.split())

# print(count_words)    



# Q9. Write a program to read a CSV file and print its contents.

# import csv

# with open("student.csv", "r") as file:
#     readcontent= csv.reader(file)

#     for row in readcontent:
#         print(row)


# Q10. Handle multiple exceptions in a single try block.

# try:
        
#     a=int(input("enter a  : "))
#     b=int(input("enter b  : "))

#     print(a/b)
# except ZeroDivisionError:
#     print("cannot divisible by zero")

# except ValueError:
#     print("entered wrong value")
