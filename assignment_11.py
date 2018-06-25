###############################################################################

#Q.1- Create a class Animal as a base class and define method animal_attribute.
#Create another class Tiger which is inheriting Animal and access the base class method.

class Animal():
    def animal_attribute(self):
        self.age=int(input("enter age of animal:-"))
        b=self.age
        print("Age of animal is:- ",b)
class Tiger(Animal):
    def __init__(self):
        print("inherted class:-")
g=Tiger()
g.animal_attribute()

###############################################################################

'''Q.2- What will be the output of following code.

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print a.f(), b.f()
print a.g(), b.g()
'''
#We need to write
'''print a.f(), b.f()
print a.g(), b.g()
as
print (a.f(), b.f())
print (a.g(), b.g())
then output will be A B
                    A B'''
                    
###############################################################################

#Q.3- Create a class Cop. Initialize its name, age , work experience and designation. 
#Define methods to add, display and update the following details. 
#Create another class Mission which extends the class Cop.
#Define method add_mission _details. 
#Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.

class Cop:
    def add(self,name,age,work_exp,designation):
        self.name=name
        self.age=age
        self.work_exp=work_exp
        self.designaation=designation
    def display(self):
        print("name : ",self.name)
        print("age : ",self.age)
        print("work experience : ",self.work_exp)
        print("designation : ",self.designaation,"\n")
    def update(self,name,age,work_exp,designation):
        self.name = name
        self.age = age
        self.work_exp = work_exp
        self.designaation = designation

class Mission(Cop):
    def add_mission_details(self,Mission):
        self.Mission=Mission
        print(self.Mission)

m1= Mission()
m1.add_mission_details("Assigned for Petrolling")
m1.add("Abhinav",22,2,"Inspector")
m1.display()
m1.update("Jatin",24,6,"Staff Inspector")
m1.display()

###############################################################################

#Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area.
#Create class rectangle and square which inherits shape and access the method Area.

class Shape:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth

    def Area(self):
            print("Area  is %d"%(self.l*self.b))


class Rectangle(Shape):
    def __init__(self,ln,bd):
        self.lengthh=ln
        self.bdd=bd


    def Area(self):
        print("Area of rectangle is : %d"%(self.lengthh*self.bdd))

class Square(Shape):
    def __init__(self,s):
        self.side=s

    def Area(self):
        print("Area of Square is :%d"%(self.side*self.side))


obj=Rectangle(5,6)
obj1=Square(4)
obj.Area()
obj1.Area()

###############################################################################