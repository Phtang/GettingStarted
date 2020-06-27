#Python Basics for Data Science
#IBM: PY0101EN
#Module 3

#Topics: Comparison Operators, Loops

################################################################################################################################################

#Comparison Operators
# ==, <, >, >=, <=, !=
#applies to ints and floats, strings

# == operator checks two values for equality and outputs a boolean
A=3
B=4
print(A==B)

# != checks inequality
print(A!=B)

#Branching (IF Statements); no need to "end"
age=20
if age>21:
    print("party time")
elif(age==20):
    print("kids table")
else:   
    print("bye")

#Logic Operators
#NOT, OR, AND

################################################################################################################################################

#Loops
Colours=["red","Yellow","Blue","Orange"]

#For lists
for i in range(0,2): #range does not include last number
    Colours[i] = "white"

print(Colours)

#For Tuples
Colours={"red","Yellow","Blue","Orange"}
for i in Colours: #For sets or tuples, you don't need to state range
    print(i)


for i,Colours in enumerate(Colours): #Enumerate could be a good function to match index with element
    print(i,Colours)

#While Loops
Colours2=["red","red","red","Yellow","Blue","red","Orange"]
j=0
NewColour=[]
while Colours2[j]=="red":
    NewColour.append(Colours2[j]) #Extend function will add letter by letter, as Append adds as an element
    j=j+1
print(NewColour)

################################################################################################################################################

#Functions

def add4(a):
    """
    Use triple quotes to document functions
    """
    b=a+4

    return b

c=add4(6) #calling a function

def printer(): #Can exist without a Return statement
    print("I did nothing")

printer()

#Note that z is not defined in the function, however it is defined before the funciton is called
#Python will search for local variables then global variables to make the function successful
def Scope(x):
    y=z+x+5 
    return y

z=6 
W=Scope(3)
print(W)

def globe():
    global vari  #Since this was defined as a global variable, it can be used outside of the function once the function is called below
    vari=15

globe()
print(vari)

################################################################################################################################################

#Objects and Classes
#Types: INT, float, string, list, dictionary, bool - each is an object
#Every object has a type, internal blueprint, and methods(set of procedures for interacting with object)
#Object is an instance of a particular type

#For example, .Sort() is a method for type lists or objects of lists
Ratings=[1,5,3,2,9,3]
Ratings.sort()
print(Ratings)

#Classes; Have data attributes and methods
#2 examples
#Class: Circles; attributes: Colour and radius
#Class: Rectangle: attributes: length, width, colour

#init is a "constructor" and tells python you are creating a new class
class Circle(object):
    def __init__(self,radius,colour): 
        self.radius=radius;
        self.colour=colour;
    #METHODS
    def add_radius(self,r):
        self.radius = self.radius+r
    

class Rectangle(object):
    def __init__(self,height, width,colour): #init is a "constructor" and tells python you are creating a new class
        self.radius=height;
        self.radius=width;
        self.colour=colour;

#The "self" parameter is kind of a grouping of attributes
#Call on classes below

C1 = Circle(10,"red")
C1.radius #calls on specific parameter
C1.colour="orange" #Can change attributes on the fly

#Calling the method
C1.add_radius(15)
#drawcircle

# dir() function is useful for obtaining the list of data attributes and methods associated with a class

#Lab
class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1

car1=Car('Honda','Accord','blue')
car1.sell()
car1.car_info()
