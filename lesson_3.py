"""Error Handling, File Handling, Modules """


# -----------------------------------------Exception Handling---------------------------------------

# Errors occur due to mistakes in the code that prevent it from running. These can be syntax errors or logical errors

# Syntax error ,
# Indentation Error ,
# Tab error

# -----------------Exceptions-------------

# Exceptions are unexpected events or errors that occurs during the execution of a program, which disrupts the normal flow of the program.


# Keyword                         Purpose

# try  ===== # Wrap the block of code that might cause an exception.

# except ==== # Handle the exception if it occurs

# # else  ==== # Run code only if no exception occurs

# finally  ==== # Run code no matter what, whether there’s an exception or not

# raise   ===== # Manually throw an exception



# a= int(input("enter the number : "))

# try:
#     print(10/a)  
# except Exception as err:
#     print(f" there is an error as {err}")
# else:
#     print("there is no exception")

# finally:
#     print("i will run no matter what")


# print("ok i have done the division")


# age = int(input(" enter your age  : "))


# try:

#     if age<10 or age>18 :
#         raise ValueError(" your age must be between 10 and 18")
#     else:
#         print("welcome to the club")

# except Exception as err:
#     print(f" an error occured as{ err}")
    
# print("the club will start soon ")    

# -----------------file handling--------------





# File handling means Creating, Reading, Updating, Deleting(CRUD) operations that we can perform in files
# Now lets see how to perform these operations in python.
# We have to use open() function to open a file in python.



# Now there are multiple modes to open the file.

# Mode                                     Description

# ‘r’                                    Read (default) – file must exist.

# ‘w’                                    Write – creates file or overwrites.

# ‘a’                                    Append – adds to end of file.

# ‘x’                                    Create – creates a new file, fails if it exists



# p = open(r'C:\Users\Tushar Panwar\Desktop\rr.txt')
# p = open('lesson_3.py')
# print(p.read())

# p.close()

# e=  open("add.txt",'w')  # just run to create or overwrite 
# e.write("helllo this is my file ")

# e=  open("add.txt",'a')  # just run to append using a


# e.write("now i am append this text in this file ")


# e.close()

# f= open("new.txt", 'x')  # to create new file

