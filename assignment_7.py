#
###############################################################################

#Q.1- Create a function to calculate the area of a circle by taking radius from user.

def area_circle(rad):
    area = 3.14*rad*rad
    return area

a=int(input("Enter radius of the circle: "))
print("area of the circle of radius ",a," is ",area_circle(a))

###############################################################################

#Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].

def perfect(n):
    sum=1
    i=2
    while (i*i)<=n:
        if n%i==0:
            sum=sum+i+n/i
        i=i+1
        return(True if sum==n and n!=1 else False)
a= int(input("Enter any no. : "))
if perfect(a):
    print(a," is a pefect no.")
else:
    print(a," is not a pefect no.")   
    
###############################################################################

#Q.5- Write a function to find factorial of a number but also store the factorials calculated in a dictionary

def fact(x):
    if x==1:
        return 1
    else:
        return (x * fact(x-1))

a= int(input("Enter any Number: "))
print("factorial of ",a," is ",fact(a))

###############################################################################