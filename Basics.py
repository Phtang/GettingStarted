#Python Basics for Data Science
#IBM: PY0101EN
#Module 1

#Hello Test
print("Hio")

# Check Python Version
# import sys
# print(sys.version)

#Checking type of variables
print(type(1))
print(type(1.0))

#Converting object types
print(type(float(1)))
print(type(int(1.0)))
print(type(int('1')))
print(type(float("1.0")))

#Strings
Name="Peter Tang"
print(Name[::2]) #every other letter
print(Name[0:5:2]) #every other letter for first 5
print(len(Name)) #length
print(Name + " is \t learning \n Python") 
print(2*Name)

#Methods for Strings
Uppercase=Name.upper() #All uppercase
print(Uppercase)

Replace=Name.replace('Peter', 'Andrew') #replace text
print(Replace)

print(Name.find('r')) #Finds text. Note: Count starts from 0