# -*- coding: cp1252 -*-
###############################################################################

Q.1- What is Time Tuple?
A time tuple is the usage of a tuple (list of ordered items/functions) for the ordering and notation of time.
The tuple used for time in Python-based systems can be largely summarized as ordering by 
year (value of 1970 or higher) 
month (1 to 12)
day (1 to 31)
hour (0 to 23) 
minutes (0 to 59) 
seconds (0 to 59) 
day of the week (0 to 6, where 0 = Monday and 6 = Sunday) 
day of the year (1 to 366) and finally a DST (Daylight Savings Time) value of either -1 (“fall back”), 0 (“normal”), +1 (“spring forward”).

Thus, I could define the moment of The Epoch (An important moment in Unix systems) as being the following: 1970 1 1 0 0 0 3 1 0 (I may not have formatted that perfectly, memory is a little fuzzy on this). 
This would translate to a string reading as “Thu Jan 1 00:00:00 1970”.

Basically, the tuples for time are just a way of ordering the values for any given specific moment in time.

###############################################################################

Q.2- Write a program to get formatted time.
import datetime
x = datetime.datetime.now()
print(x.strftime("%H:%M:%S"))

###############################################################################

Q.3- Extract month from the time.
import datetime
x = datetime.datetime.now()
print("current month : ")
print(x.strftime("%B"))

###############################################################################

Q.4- Extract day from the time.
import datetime
x = datetime.datetime.now()
print("current day : ")
print(x.strftime("%A"))

###############################################################################

Q.5- Extract date (ex : 11 in 11/01/2021) from the time.
import datetime
x = datetime.datetime.now()
print(x.strftime("%d"))

###############################################################################

Q.6- Write a program to print time using localtime method.
import time
x=time.localtime(time.time())
print("Local time : ",x)

###############################################################################

Q.7- Find the factorial of a number input by user using math package functions.
import math 
x=int(input("factorial of "))
print("factorial is ",math.factorial(x))

###############################################################################

Q.9- Use OS package and do the following tasks: 
1. Get current working directory.
import os
print(os.getcwd())

2. Get the user environment.
import os
print(os.environ)

###############################################################################

