#Python Basics for Data Science
#IBM: PY0101EN
#Module 2: Python Data Structures

#Topics: Tuples, Lists, Sets

################################################################################################################################################

#Tuples
#Note: Cannot change array elements of tuple (immutable)
Tuple1=("Hike",10.3,"Beach") #Array of different elements
Tuple2=(3,5,7.7)
print(Tuple1[2]) #Slice tuples

Tup_comb=Tuple1+Tuple2
print(Tup_comb) #combine

print(Tup_comb[3:5]) #slice

print(len(Tup_comb)) #find length

Tup_sort=sorted(Tuple2)
print(Tup_sort) #Can sort if it is all numerical objects

#Nesting Tuples
Tup_nest=(1,3,("Hi","Bye"), (4,5))
print(Tup_nest[2])
print(Tup_nest[2][0]) #Can access nest within tuple
print(Tup_nest[2][0][1]) #Can access another layer into the string

################################################################################################################################################

#Lists; represented by square brackets[], NOT immutable- can change elements
List1=[1,4,6]
List2=["Yo","Sup",5]

List1[0]=5 #Mutable example
print(List1) 

List1.extend([99,100]) #Extendable list
print(List1) 

List2.append(["new","test"]) #append new item(s) as 1 element
print(List2)

del(List1[1]) #Deletes specific array element
print(List1) 

print("a,b,c,d".split(",")) #Can split string based on what is defined in Split(); use as a delimiter

List_Clone=List1[:] #The [:] syntax clones list as separate instead of copying the whole thing
print(List_Clone)

print(List_Clone[-1]) #Can use negative indexing for lists and tuples, which go in reverse sequence
print(List1[1:])#Syntax to remove the first element

################################################################################################################################################

#Sets; Do not record element position; defined by {}; just a jumble of elements
Set1={3,6,7}
Set2={"Halls","Reese","Coffee",3}

#Duplicates in the set are deleted. Therefore, 4 is only shown once
List_set=[1,4,4,6]
print(set(List_set))

Set2.remove("Halls") #Can remove specific elements this way
print(Set2)

print(3 in Set1) #Check whether something exists in set. Returns bool

Set_common= Set1 & Set2 # & Finds cross-section/common elements between sets
print(Set_common)

set_union=Set1.union(Set2) #Combine sets
print(set_union)

print(Set_common.issubset(Set1)) #Checks for subsets. i.e. if the first set exists within the second set of elements


################################################################################################################################################

#Dictionaries
#Similar to Lists, except the element in the array does not have to be defined by a number
#Defined by {}
#The key is followed by the element inside the dictionary.
#Keys are immutable and unique

Dict1={"peter":24,"Rachael":33, ("Dad","Mom"):63}
Ref1=Dict1[("Dad","Mom")] #This is how you reference Keys
print(Ref1)

Dict1["Young"]=10 #Simply add new entries
print(Dict1)

del(Dict1["Young"]) #Deletes the specific Key and element

"Mom" in Dict1 #Check if it exists in the Dictionary

print(Dict1.keys()) #Outputs all keys
print(Dict1.values()) #Outputs all elements/values