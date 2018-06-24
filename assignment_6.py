###############################################################################

#Q.1- Take 10 integers from user and print it on screen.

i=0
l=[]
while(i<10):
  y=int(input("enter the no."))
  l.append(y)
  i=i+1
for i in l:
    print(i)

###############################################################################

#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.

count = 10
while(count>0):
   print("infinite loop")

###############################################################################

#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.

l1=[]
for x in range(5):
   y = int(input("Enter an integer value: "))
   l1.append(y)

print("Entered list is: ",l1)
l2=[]
for x in l1:
   z = x*x
   l2.append(z)

print("Updated list is: ",l2)

###############################################################################

#Q.4- From a list containing ints, strings and floats, make three lists to store them separately.

l1 = [1,2,'abc',7,6.4,'xyz',2.8]
l2 = []
l3 = []
l4 = [] 
for x in l1:
   if  type(x) == int:
      l2.append(x)
   elif type(x)== str:
      l3.append(x)
   elif type(x) == float:
      l4.append(x)

print("List of integers: ",l2)
print("List of strings: ",l3)
print("List of floats: ",l4)

###############################################################################

#Q.5- Using range(1,101), make a list containing even and odd numbers.

even=[]
odd=[]
for x in range(1,101):
    if(x%2==0):
        even.append(x)
    else:
        odd.append(x)

print("List of even numbers: ",even)
print("List of odd numbers: ",odd)

###############################################################################

#Q.6-Print the following patterns:

p = 1
while(p<=4):
    print("*"*p)
    p = p+1
    
###############################################################################

#Q.7- Create a user defined dictionary and get keys corresponding to the value using for loop.

d = {'One':1,'Two':2,'Three':3,'Four':4}
for x in d.keys():
    print(x,d[x])

###############################################################################

#Q.8- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.

l1=[]
s = int(input("Enter the size of list"))
for x in range(s):
    y = int(input("Enter value: "))
    l1.append(y)
d = int(input("Enter element to be deleted"))
for x in l1:
    if x == d:
        l1.remove(x)
    else:
        print("Element not in the list")
print("The list is: ",l1)

###############################################################################





