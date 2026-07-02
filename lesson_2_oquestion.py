'''IN THIS WE DO SOME QUESTIONS BASED ON LESSON 2 : TOPICS ARE:'''

# ----------------Functions, Lists, Tuples, Dictionaries, Sets---------------


# 1. Write a function to check if a number is even.



# def even(n):
#     if n%2==0:
#         return True
#     else:
#         return False





# num=int(input("enter the number to check if number is even or odd using function :  "))

# if even(num):
#     print("even number")
# else:
#     print("odd number")    


# 2. Create a list and find the sum of all its elements.

# l= [34,21,45,75,5]

# sum=0

# for i in l:
#     sum+=i

# print(sum)    



# 3. Write a program to find the maximum and minimum in a list.(give atleast two method to solve)


# l= [23,45,76,2,45,765,34,222,999,10000,34,65,95678,1,343]

# # first method
# # print(f"maximum number in this list is : {max(l)}")
# # print(f"maximum number in this list is : {min(l)}")

# # second method

# max_num=l[0]
# min_num=l[0]

# for i in l:
#     if i>max_num:
#         max_num=i
#     elif i<min_num:
#         min_num=i

# print(f"the maximum n is : {max_num} and the minimum n is {min_num}")


# 4. Create a program that removes duplicates from a list.(solve it with in two types)


# l=[1,2,3,3,3,4,4,4,5,5,6,7,8,9,9,7,5]

# # # first method 
# # remove_dupli=list(set(l))
# # print(l,"\n")
# # print(remove_dupli)      

# new_lunique=[]

# for i in l:
#     if i not in new_lunique:
#         new_lunique.append(i)

# print(new_lunique)        



# 5. Write a function to reverse a list.

# def reverselist(lst):           #first method
#     return lst[::-1]


# def reverselist(lst):           #second method
#     lst.reverse()
#     return lst


# l=[4,2,56,7]

# print(reverselist(l))


# # 6. Create a tuple and access its elements.


# tup=(2,3,4,5,5,5,7,4,28,"mango",78)

# print(tup[0])
# print(tup[2])
# print(tup[3])
# print(tup[4])
# print(tup[6])
# print(tup[9])


# 7. Convert a list into a tuple and vice versa.

# l=[2,3,4,5,6,7]

# t=tuple(l)

# print(type(t),  t)

# new_l=list(t)
# print(type(new_l),  new_l)

# 8. Write a program to merge two dictionaries.

# di= {10:111, 20:345,30:342, 40:700}
# d2= {60:199, 50:366,70:362, 80:900}


# # for i in d2:             #first method
# #     di[i]=d2[i]

# di.update(d2)  # second method
# print(di)



# 9. Write a function to count the frequency of elements in a list.



# def frequency(l):
#     dis_fre={}
#     for i in l:
#         if i in dis_fre:
#             dis_fre[i]=dis_fre[i]+1
#         else:
#             dis_fre[i]=1
#     return dis_fre





# l=[1,2,3,3,3,4,4,4,5,5,6,7,8,9,9]

# print(frequency(l))



# 10. Create a dictionary of squares of numbers from 1 to 10.

# d={}

# for i in range(1,11):
#     d[i]= i*i

# print(d)


# 11. Write a program to sort a list in ascending order.

# l=[2,5,1,7,9,3,1]

# # l.sort()   #.sort will change or sort the original list 

# new_list=sorted(l)   # sorted will not change the main list 

# print(new_list)

# print(l)

# 12. Create a program to check if a key exists in a dictionary.

# dic= { "name": "aakash",
#       "age": 24,
#       "monthly_salary": 300000}


# key =input("enter the key to check if that is present or not:  ")

# if key in dic:
#     print(f"key is present, enterd key :  {key}")
# else:
#     print(f"key is not present : enterd key == {key}")    



# 13. Create a set and perform union, intersection, and difference.

# aset={2,3,4,6,7,8}
# bset={2,4,3,6,7,3}

# print(aset - bset)    # difference
# print(aset&bset)    # intersection
# print(aset|bset)    # union

# g={}

# print(type(g))


# 14. Write a function to find common elements in two lists.


# def commonlist(l1,l2):
#     common=[]
#     for i in l1:
#         if i in l2:
#             common.append(i)

#     return common        

# a=[1,2,3,5,6,7,8,22,9]
# b=[2,3,4,5,6,7,7,22,8]

# print(commonlist(a,b))


# 15. Write a function that returns the factorial of a number.


# def factorial(f):

#     fact=1
#     for i in range(1,f+1):
#         fact=fact*i

#     return fact

# n=5
# print(factorial(n))


# 16. Create a function that checks whether a string is a palindrome.

# def palindrome(str):
    

#     if str ==  str[::-1]:
#         return "palindrome"
#     else:
#         return "not palindrome"



# name=input("enter the name:  ")

# print(palindrome(name))


# 17. Write a function to count vowels in a string.

# def countvowe(a):

#     count=0
#     for i in a:
#         if i in "aeiouAEIOU":
#             count+=1
#     return count

# str=input("enter the string to count vowels ")

# print(countvowe(str))

# 18. Create a dictionary and iterate over its keys and values.

# dic={"name":'ganesh',
#      "age": 23,
#      "job_profile": "ai engineer"}

# for key, value in dic.items():
#     print(key,"=",value)


# 19. Write a function to remove all punctuation from a string.

# import string

# def remove(strrr):

#     result=""
#     for i in strrr:
#         if i not in string.punctuation:
#             result+=i
#     return result

# strr="hello,?!!!!"        

# print(remove(strr))





# 20. Write a function to capitalize the first letter of each word in a string.

# def capitalize(a):
#     return a.title()

# sentence= input("enter any sentence or statement to capitalize:  ")
# print(capitalize(sentence))


# 21. Create a list comprehension to get squares of all even numbers in a range.

# square= [i*i for i in range(1,11) if i%2 ==0]

# print(square)

# 22. Write a function to check if a string is an anagram.


# def anagram(w1,w2):
#     if sorted(w1)== sorted(w2):
#         return "this is anagram"
#     else:
#         return "this is not anagram"

# a= input("enter the word 1:   ")
# b= input("enter the word 2:   ")

# print(anagram(a,b))

# 23. Create a nested dictionary to represent student records.



# student= { "student1":{ "name":"rahul", "age": 23, "marks": 100 },
          
          
#           "student2":{"name":"tushar", "age": 24, "marks": 100 }
          
#           }

# print(student)



# 24. Write a function to flatten a nested list.


# def flatten(l):
#     new_l=[]
#     for i in l:
#         for j in i:
#             new_l.append(j)
#     return new_l


# lst=[[1,2],[3,4],[5,6]]
# print(flatten(lst))


# 25. Write a program to find the second highest number in a list.(do with sort and loop , give 2 solution sort and another one from using loop)

# l=[2,4,63,1,6,85,4,6,222,774,98,55,34,656]
# l = [80, 60, 40]
# l.sort()                   

# second_largest=l[-2]    #first method using sort

# print(second_largest)

# second method using loop

# largest = second = float("-inf")        #this  means that negative infinite number use is the smallest value 

# numbers = [30, 70, 40]

# for i in numbers:
#     if i > largest:
#         second=largest
#         largest=i
#     elif i >second:
#         second=i
# print(f"this is the largest num : {largest}")
# print(f"this is the second largest: {second}")

# 26. Create a function to rotate a list left by k positions.

# def rotate(l,k):
#     return l[k:]+ l[:k]




# l=[1,2,3,4,5,6,7,8,9]

# b=int(input("enter the num to where rotate the list"))

# print(rotate(l,b))



# 27. Write a function to find the missing number from a list of 1 to N.

# def mis_num(l,n): 

#     exp= n*(n+1)//2
#     actual=sum(l)
#     return exp-actual



# listt = [1,2,3,4,5,6,8,9]


# print(mis_num(listt,9))


# 28. Write a program to remove all None values from a list.

# l=[1,2,3,None,5,6,None,8]

# n=[]
# for i  in l:
#     if i is not None:
#         n.append(i)

# print(l)
# print(n)

# 29. Write a function to merge two dictionaries and handle key collisions by summing values.


# def merge(dist1,dist2):

#     result=dist1.copy()

#     for key, value in dist2.items():

#         if key in result:
#             result[key]+=value
#         else:
#             result[key]=value
#     return result



# d1={10:100,20:200,30:300}
# d2={30:100,40:200,50:300}

# print(merge(d1,d2))


# 30. Create a function to find unique elements present in only one of two lists.


# def unique(a,b):

#     set1=set(a)
#     set2=set(b)

#     return list(set1^set2)

# l1=[1,2,3,4,5,6]
# l2=[5,6,7,8,9,10]

# print(unique(l1,l2))