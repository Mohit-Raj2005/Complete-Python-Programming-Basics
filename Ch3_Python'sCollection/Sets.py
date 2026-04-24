#creating a set
names={"satyam","ekta","bashu","rohan"}
print(names) # everytime we print names... new order will be seen

#check length of the set
print("length",len(names) ,"type:",type(names))

#accesing elements of set using for loop since indexing is not there in sets
for x in names:
    print(x)

#check if an item exists in a set or not
if "bashu" in names:
    print("bashu is present in the names")

#we can add elements in a set using add() function
names.add("SHREENIKA")
print(names)

#add another sequence such as a list etc to the sets using update() fuinction
nameList=["A","B","C","D","E"]
names.update(nameList)  #updatea() function adds this namelist to the set
print(names)

#removing elements from a set using remove() function
print("remove ekta using remove and discard function")
print("using remove() function")
names.remove("ekta") #removing ekta from the set
print(names)

#we can also use discard() function... this function will not throw error if the name is not present 
print("using discard() function")
names.discard("ekta")
print(names)


#joining two sets using union() function
s1={"a","b","c","d","e"}
s2={"d","e","f","g","h"}
print(s1,s2)
s3=s1.union(s2)
print("using union function")
print(s3)
#we can also use update() function]
print("using update function")
s1.update(s2)
print(s1)

#we can keep only duplicates also by usin intersection_update() function
print("using intersectionupdate function")
s1.intersection_update(s2)
print(s1)

#we can keep all values except duplicates or can say complement of two set using summetric_difference_update() function
print("using symmetric_difference_update function")
s1.symmetric_difference_update(s2)
print(s1)