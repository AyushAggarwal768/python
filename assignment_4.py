###############################################################################
#Q.1- Write a program to create a tuple with different data types and do the following operations.
#1. Find the length of tuples

tup = (1,2,'Ayush',(1,2))
print(len(tup))

###############################################################################

#Q.2-Find largest and smallest elements of a tuples.

tup=(1,3,9,2,4,0,7,8,6)
print("maximum value is: ",max(tup))
print("minimum value is: ",min(tup))

###############################################################################

#Q.3- Write a program to find the product of all elements of a tuple.

tup = (1,5,2,7,4,9)
product=1
for x in tup:
    product = product*x
print("product: ",product)

###############################################################################

#sets
#Q.1- Create two set using user defined values. 
#1. Calculate difference between two sets.
#2. Compare two sets.
#3. Print the result of intersection of two sets

set1={2,1,3,4,6,7}
set2={1,4,7,5,8}
print("difference: ", set1 - set2)
print("comparison: ", set1<=set2)
print("intersection: ", set1 & set2)

###############################################################################

#dictionaries
#Q.1- Create a dictionary to store name and marks of 10 students by user input.

dict = {}
for i in range(10):
    name = input("enter name")
    marks = int(input("enter marks"))
    dict[name] = marks
print(dict)

###############################################################################

#Q.3- Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.

dict={}
str = "MISSISSIPPI"
m = str.count('M')        
i = str.count('I')
s = str.count('S')
p = str.count('P')
dict['M']= m
dict['I']= i
dict['S']= s
dict['P']= p
print(dict)






