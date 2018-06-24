###############################################################################

#Q.1-Take an input year from user and decide wheather it is leap year or not.

year = int(input("Enter the year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("%d is a leap year" %(year))
       else:
           print("%d is not a leap year" %(year))
   else:
       print("%d is a leap year" %(year))
else:
   print("%d is not a leap year" %(year))

###############################################################################

#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
if (l==b):
    print("It is a sqaure")
else:
    print("It is a rectangle")
    
###############################################################################

#Q.3- Take the input age of 3 people and determine oldest and youngest among them.

x=int(input("Enter a age of x: "))
y=int(input("Enter a age of y: "))
z=int(input("Enetr a age of z: "))
if(x<y and x<z):
    print("x is youngest")
elif(y<x and y<z):
    print("y is youngest")
elif(z<x and z<y):
    print("z is youngest")
elif(x>y and x>z):
    print("x is oldest")
elif(y>x and y>z):
    print("y is oldest")
elif(z>x and z>y):
    print("z is oldest")
else:
    print("ages are same")
    
###############################################################################

#Q.4- Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points(your input). points can only take on positive integer values up to 200.
#If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. If there's no prize, the message should state "Sorry! No prize this time."
#Points	Prize
#1-50	 No Prize
#51-150	 Wooden Dog
#151-180 Book
#181-200 Chocolates


points = int(input("Enter points : "))
if (points > 0 and points <= 50):
    print("Sorry! No prize this time!")
elif(points > 50 and points <= 150):
    print("Congratulations! You have won a Wooden Dog")
elif(points > 150 and points <= 180):
    print("Congratulations! You have won a Book")
elif(points > 180 and points <= 200):
    print("Congratulations! You have won a Chocolates")
    
###############################################################################

#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

quantity = int(input("Enter the quantity of items: "))
cost = quantity*100
if cost > 1000:
    print("You got 10% discount")
    discount = (cost*10)/100
    updated_cost = cost-discount
    print("You need to pay %d" %(updated_cost))
else:
    print("You need to pay %d" %(cost))

###############################################################################