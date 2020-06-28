#Python Basics for Data Science
#IBM: PY0101EN
#Module 4: Working with Data in Python

#Topics: Reading/writing files, Pandas

################################################################################################################################################

#Reading/Writing files
# #File1=open("/resources/date.txt","w"); The path is the file. The 2nd element is command - read(r), write(w), append(a)
# File1=open('/Users/Peter Tang/Desktop/Python/GettingStarted/GettingStarted/Example1.txt','r')
# Filename=File1.name
# print(File1)
# print(Filename)
# File1.close() #Closes file. May get tedious, so use With statement

with open("Example1.txt","r") as File1: #This works if the .txt file exists in the same folder as .py
    contents=File1.read()
    print(contents)


print(File1.closed) #check if file is closed
print(contents) #Can print contents outside of With

#For some reason, With only likes to use a "read" command once, so using other reads (readlines) requires another With statement
with open("Example1.txt","r") as File1: #This works if the .txt file exists in the same folder as .py
    contents_lines=File1.readlines() #Categorizes each line in the .txt file as an array index

with open("Example1.txt","r") as File1: #This works if the .txt file exists in the same folder as .py
    contents_line1=File1.readline() #Readline starts off by reading first line
    contents_line2=File1.readline() #Next time it is called, it reads the next line in sequence. Can be looped

print(contents_lines[0]) #Line1
print(contents_lines[1]) #Line2
print(contents_lines[2]) #Line3

print(contents_line1[0]) #Index 0 of Line1
print(contents_line2[4]) #Index 4 of Line2

with open("Example1.txt","r") as File1: #This works if the .txt file exists in the same folder as .py
    #Putting a value in the "readlines" method will output the first x charactrs of that line.
    #When "readlines" is called again, it jumps to the next line
    contents_part=File1.readlines(3)
    print(contents_part)
    contents_part=File1.readlines(7)
    print(contents_part)
    contents_part=File1.readlines(4)
    print(contents_part)