# Q1
# Input= "Sky is blue"
# Output= "blue is sky"
#
# str1="sky is blue"
# my_list= str1.split()
#  my_list= my_list[::-1]
#  my_list2=" ".join(my_list)
# print(my_list2)
# print(" ".join(str1.split()[::-1]))
#
# Q2
# List =[1,2,2,3,3,4,5,5,5,6,6]
# Output:- [1,4]

# my_list=[1,2,2,3,3,4,5,5,5,6,6]
# new_list=[]
# for num in my_list:
#     if my_list.count(num)==2:
#         new_list.append(num)
# print(new_list)


#############################################.........................................................................


#Q1 HOW TO SWAP TWO NUMBERS
#APPROACH 1

# num1 = 10
# num2 = 20
#
# num1,num2= num2,num1
# print(num1,num2)

#Approach 2

# num1= 10
# num2= 20
#
# temp=num1
# num1=num2
# num2=temp
#
# print(num1,num2)


#Q2 HOW TO CHECK A NUMBER IS PRIME OR NOT

# num=44
# count= 0
#
# if num>0:
#     for i in range(1,num+1):
#         if num%i==0:
#             count=count+1
#
#     if count==2:
#         print("prime number")
#     else:
#         print("not a prime number")
#
# if num==0:
#     print("invalid")

#Q3 HOW TO FIND FACTORIAL OF A NUMBER

# factorial=1
# num= 4
#
# if num<0:
#     print("factorial doesnt exist for negative numbers")
#
# if num==0:
#     print("factorial for number 0 is 1")
#
# if num>1:
#     for i in range(1,num+1):
#         factorial=factorial*i

#print(factorial)

#Q4 HOW TO PRINT FIBONACCI SERIES

# 0 1 1 2 3 5 8 13 21 34

# n1 = 0
# n2 = 1
# print(n1)
# print(n2)
# for i in range(1,10):
#     sum=n1+n2
#     print(sum) #1 #2 #3
#     n1=n2 #1 #1 #2
#     n2=sum # #2 #3

#Q5 SUM OF ELEMENTS IN AN ARRAY
#INPUT: ARR[]= {1,2,3}
#OUTPUT: 6
# 1+2+3=6

# arr=[1,2,3,4,5,]
# print(sum(arr))
# print(sum(arr,10))
# print(sum(arr,-10))

#Q6 HOW TO FIND MAX AND MIN NUMBER IN ARRAY
#input: arr[] = [10,20,4]
#output : 20
#input : 10


# arr= [2,5,34,4,9]
# max= arr[0]
# n= len(arr)
#
#
# for i in range(1,n):
#     if max<arr[i]:
#         max=arr[i]
#
# print(max)


#Q8 HOW TO FIND LENGTH OF A LIST

# mylist=[1,4,6,7,8]
#
# count=0
# for i in mylist:
#     count= count+1
# print(count)


#Q9 SWAP FIRST AND LAST ELEMENTS IN A LIST
#INPUT: [12,35,9,56,24]
#OUTPUT: [24,35,9,56,12]

#APPROACH1: TEMPORARY VARIABLE
# mylist= [3,5,7,9,0]
# size= len(mylist)
#
# temp= mylist[0]
# mylist[0]= mylist[size-1]
# mylist[size-1]= temp
#
# print(mylist)

#APPROACH2:

# mylist[0],mylist[4]= mylist[4],mylist[0]
# print(mylist)

#APPROACH3 : USING TUPLE

# get= mylist[-1],mylist[0]
# mylist[0],mylist[-1]= get
# print(mylist)

#APPROACH4: *OPERAND

# start,*middle,end= mylist
# mylist= end,*middle,start
# print(mylist)

#APPROACH5 using pop()

# first=mylist.pop(0)
# last=mylist.pop(-1)
#
# mylist.insert(0,last)
# mylist.append(first)
#
# print(mylist)


#Q10 SWAP ANY TWO ELEMENTS IN A LIST
#INPUT: LIST=[23,65,19,90], pos=1, pos=3
#OUTPUT: [19,65,23,90]

#APPROACH1: SIMPLE SWAP
# mylist=[23,65,19,90]
#
# mylist[2],mylist[0]= mylist[0],mylist[2]
# print(mylist)


#APPROACH2: USING INBUILT LIST.POP() FUNCTION

# mylist=[23,65,19,90]
#
# pos1,pos2= 1,3
#
# first_element= mylist.pop(pos1)
# second_element= mylist.pop(pos2-1)
#
# mylist.insert(pos1,second_element)
# mylist.insert(pos2,first_element)
#
# print(mylist)

#APPROACH3: USING TUPLE

# mylist=[23,65,19,90]
#
# pos1,pos2=1,3
# get= (mylist[pos1],mylist[pos2])
# mylist[pos2],mylist[pos1]= get
#
# print(mylist)


#Q11 REMOVE NTH OCCURRENCE OF THE GIVEN WORD {have to come back on this}

# mylist=["geeks","for","geeks",]
# word= "geeks"
# n=2
# count=0
#
# for i in range(0,len(mylist)-1):
#     if(mylist[i]==word):
#         count=count+1
#         if(count==n):
#             del mylist[i]
# print(mylist)

#Q12 HOW TO SEARCH ELEMENT IN A LIST
#APPROACH 1
# mylist=[2,5,7,0,9,4]
# ele=100
# flag=0
# for i in mylist:
#     if(i==ele):
#         print("element found")
#         flag=flag+1
#         break
#
# if flag==0:
#     print("element does not found")

#APPROACH2
# mylist=[2,6,8,0,3,9]
# ele=8
#
# if ele in mylist:
#     print("elements found")
# else:
#     print("element doesnt found")


#Q13 HOW TO CLEAR A LIST

#APPROACH1
# mylist= [2,5,8,9,0]
# print("print before initialize",mylist)
# mylist=[]
# print("print after initialize",mylist)

#APPROACH2

# mylist=[3,4,5,6,7]
# mylist.clear()
# print(mylist)

#APPROACH3

# mylist=[3,4,7,3,7]
# del mylist[:]
# print(mylist)

#APPROACH4

# mylist=[4,6,4,7,4]
# mylist*=0
# print(mylist)


#Q14 HOW TO REVERSE A LIST

#APPROACH1
# mylist=[3,4,5,6,7,8]
# mylist.reverse()
# print(mylist)

#APPROACH2

# mylist=[3,4,5,67,6]
# mylist=mylist[::-1]
# print(mylist)

#Q15 HOW TO CLONE OR COPY A LIST

#APPROACH1: USING SLICING TECHNIQUE
# mylist=[3,5,7,9,1]
# mylist_copy= mylist[:]
# print(mylist_copy)

# #APPROACH2: EXTEND METHOD
# mylist=[2,5,6,8,9,9]
# mylist_copy=[]
# mylist_copy.extend(mylist)
# print(mylist_copy)

# #APPROACH3 COPY METHOD:
# mylist=[2,4,6,7,8,9]
# mylist_copy=mylist.copy()
# print(mylist_copy)

#APPROACH4 list method
# mylist=[3,5,6,7,8,7]
# mylist_copy=list(mylist)
# print(mylist_copy)

#Approach5
# mylist=[6,4,5,5,4,3,3,9]
# mylist_copy=[i for i in mylist]
# print(mylist_copy)

#Q16 COUNT OCCCURRENCES OF AN ELEMENT IN A LIST
#APPROACH1
# mylist=[1,4,5,4,4,4,4,7,8,9,3,2,2]
# ele=2
# count=0
# for i in mylist:
#     if ele==i:
#         count=count+1
# print(count)

#APPROACH2
# mylist=[7,3,3,3,4,67,43,2,5,1]
# print(mylist.count(67))

#APPROACH3
# from collections import Counter
# mylist=[2,3,3,3,35,5,6,6]
# x=6
# dic=Counter(mylist)
# print(dic[x])

#Q17 FIND SUM OF ELEMENTS OF A LIST
#APPROACH1
# mylist=[10,10,10,10,10]
# total=0
# for i in range(0,len(mylist)):
#     total=total+mylist[i]
#
# print(total)

#APPROACH2
# mylist=[10,10,10,10,10]
# print(sum(mylist))

#Q18 MULTIPLY ALL NUMBERS IN THE LIST

#METHOD1: TRAVERSAL

# mylist=[2,3,4,4]
# prod=1
# for i in range(0,len(mylist)):
#     prod=prod*mylist[i]
# print(prod)

#APPROACH2 USING NUMPY.PROD() *INSTALL NUMPY PACKAGE
# import numpy
# mylist=[2,3,3]
# result=numpy.prod(mylist)
# print(result)

#Q19 FIND SMALLEST AND LARGEST NUMBERS IN A LIST
#APPROACH1: SORT THE LIST IN ASCENDING ORDER AND PRINT THE FIRST&LAST ELEMENTS IN THE LIST
# mylist=[2,3,3,2,10,15]
# mylist.sort()
# print("smallest number is",mylist[0])
# print("largest number is",mylist[-1])

#APPROACH2: USING MIN() AND MAX()
# mylist=[2,3,36,7,8,10]
# print("smallest number is",min(mylist))
# print("maximum number is",max(mylist))

#Q20 FIND SECOND LARGEST NUMBER IN A LIST
# mylist=[3,3,9,4,10,32]
# mylist.sort()
# print(mylist[-2])

#Q21 HOW TO CHECK STRING IS PALINDROME OR NOT
#APPROACH1
#1 FIND THE REVERSE OF THE STRING
#2 CHECK IF REVERSE AND ORIGINAL ARE SAME OR NOT

# s= input("enter your string")
# reverstr= (s[::-1])
# print(reverstr)
#
# if reverstr==s:
#     print("palindrome")
# else:
#     print("not palindrome")

#Q22 REVERSE WORDS IN A STRING

# str= "welcome to the python programming"
# words= str.split(" ")
# print(words)
# words=words[-1::-1]
# outputstr= " ".join(words)
# print(outputstr)

#Q23 FIND SUBSTRING PRESENSE IN A STRING

# str= "python is the best programming"
# sub_str= "programming"
#
# print(str.find(sub_str))
#
# if (str.find(sub_str)==-1):
#     print("not found")
# else:
#     print("found")

#Q24 FIND LENGHTH OF A STRING(4 DIFFERENT WAYS)

#METHOD 1: USING FOR LOOP

# str= "welcome"
# counter=0
# for i in str:
#     counter= counter+1
#
# print(counter)

#METHOD 2: USING WHILE LOOP

# str="welcome"
# counter=0
# while str[counter:]:
#     counter= counter+1
# print(counter)

#Method 3: USING LEN METHOD
# str= "welcome"
# print(len(str))

#Q25 CHECK IF A STRING CONTAINS ANY SPECIAL CHARACTERS

# import re
# str1="$#@welcome to%^&*()__-+=?/>.<,+*/|!"
# str2="welcome to python programming"
#
# regex= re.compile('[#@!$%^&*()-_=+-*?/><,.):]')
#
# if (regex.search(str1)==None):
#     print("no special characters present in a string")
# else:
#     print("string contains special digits so its a string")







