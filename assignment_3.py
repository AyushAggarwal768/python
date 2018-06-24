###############################################################################

#Q.1- Create a list with user defined inputs.
l1=[]
a = input("enter value")
l1.append(a)
b = input("enter value")
l1.append(b)
c = input("enter value")
l1.append(c)
print(l1)

###############################################################################

#Q.2- Add the following list to above created list:
#l=['google','apple','facebook','microsoft','tesla']

l2=['google','apple','facebook','microsoft','tesla']
l1=l1+l2
print(l1)

###############################################################################

#Q.3- Count the number of time an object occurs in a list.

l1=[1,2,5,2,6,2,7,2,2]
print(l1.count(2))

###############################################################################

#Q.4- create a list with numbers and sort it in ascending order.

l1=[5,2,8,4,9,3,7,1]
l1.sort()
print(l1)

###############################################################################

#Q.5- Given are two one-dimensional arrays A and B which are sorted in ascending order.
#Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List] 

A=[2,8,6,4,3,1]
B=[9,1,5,3,7,4]
A.sort()
B.sort()
print(A)
print(B)
C=A+B
C.sort()
print(C)

###############################################################################

#Q.6-Implement a stack and queue using lists. 

#stack
l1=[]
l1.append(1)
print(l1)
l1.append(2)
print(l1)
l1.append(3)
print(l1)
print(l1.pop(-1))
print("now the list is ",l1)
print(l1.pop(-1))
print("now the list is ",l1)
print(l1.pop(-1))
print("now the list is ",l1)

#queue
l1=[]
l1.append(1)
print(l1)
l1.append(2)
print(l1)
l1.append(3)
print(l1)
print(l1.pop(0))
print("now the list is ",l1)
print(l1.pop(0))
print("now the list is ",l1)
print(l1.pop(0))
print("now the list is ",l1)

############################################################################### 
   
#Q.7- Count even and odd numbers in that list.

l1=[1,2,3,4,5,6]
even=0
odd=0
 for x in l1:
     if x%2==0:
	even+=1
     else:
	odd+=1
print("even numbers=",even)
print("odd numbers=",odd)
 
###############################################################################
 

 


 
