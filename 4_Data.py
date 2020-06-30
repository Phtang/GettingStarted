#Python Basics for Data Science
#IBM: PY0101EN
#Module 4: Working with Data in Python

#Topics: Reading/writing files, Pandas

################################################################################################################################################

#Reading files
# #File1=open("/resources/date.txt","w"); The path is the file. The 2nd element is command - read(r), write(w), append(a)
File1=open('/Users/Peter Tang/Desktop/Python/GettingStarted/GettingStarted/Example1.txt','r')
Filename=File1.name
print(File1)
print(Filename)
File1.close() #Closes file. May get tedious, so use With statement

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
    
################################################################################################################################################

#Writing files
Lines=["This is line 123 \n", "This is line B \n","This is line C \n"]

with open('Example2.txt','w') as File2: 
    
    for line in Lines:
        File2.write(line)

#Copy one file to another
with open("Example2.txt","r") as readfile:
    with open("Example3.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)

################################################################################################################################################

#Pandas: popular library for data analysis

import pandas as pd #Whenever you import, need to go to cmd and type "pip install ____" (pandas)

csv_path="CSV_file1.csv"
df=pd.read_csv(csv_path) #read_csv is a panda method

#Dataframes
songs={'Album':['Thriller','Back in Black','The Dark side of the moom','Thebodyguard'],
'Released':[1982,1980,1973,1992],
'Length':['42:19','42:11','42:49','57:44']}

songs_frame=pd.DataFrame(songs) #Create dataframe
print(songs_frame)

df1=songs_frame[['Length']] #can just grab one column of dataframe if you specify
print(df1)

print(songs_frame.head(2)) #Head method takes first two rows of data

print(songs_frame['Released']) #This syntax just obtains column without the Key

################################################################################################################################################

#Saving Data
songs2={'Album':['Thriller','Back in Black','The Dark side of the moom','Thebodyguard','Test1','Test2'],
'Released':[1982,1980,1973,1992,1982,1980],
'Length':['42:19','42:11','42:49','57:44','42:19','3']}

songs_frame2=pd.DataFrame(songs2) #must remember to put data into a DataFrame before handling
print(songs_frame2['Released'].unique()) #.unique method finds all unique elements

#Example: Find albums released after 1979, then print those specific rows
#Can do this in 1 line, but let's split up steps

print(songs_frame2['Released']>=1980) #outputs Dataframe of booleans

df2=songs_frame2[songs_frame2['Released']>=1980] #If you bracket the previous output of inequalities, it will give you the rows
print(df2)

output=df2.to_csv('new_songs.csv') #Saves new CSV file of dataframe