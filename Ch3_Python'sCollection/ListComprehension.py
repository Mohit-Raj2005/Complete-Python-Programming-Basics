#creating a new list from the elements of an exissting list

fruits=["mango","orange","guava","coconut"]
print("initial fruits list:",fruits)
newfruits=[fruit for fruit in fruits if "a" in fruit]
print("new fruit list having 'a' in them:",newfruits)


#we can also copy a list and store it into another list
#for this copy() function is used
newfruits=fruits.copy()
print("new fruit list copied from fruits list",newfruits)   #using copy() function to copy list


#we can concatinate two lists
num=[1,2,3,4,5]
newlist=fruits + num
print("new concatinated list:",newlist)


#nested lists
fruits[2]=["pear","lemon"]
print("after nesting one list to fruits list at index 2:",fruits)
print(fruits[2][0])  #printing 1st element of the nested list