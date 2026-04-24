name1='Rahul' #string i '' single quotes
name2="Mohan" #string i "" double quotes
name3='''Sohan''' #string i '''  ''' triple quotes

print(name1,name2,name3)
print(type(name1))
print(type(name2))
print(type(name3))

#we can write multiline strins in triple quotes only, in double or single quotes it will not work
paragraph='''This is a multiline string
now this one is in new line'''
print(paragraph)

#indexing in a string
print("indexing in string")
print("Index 0:",name1[0]) #Zero base indexing
print("Index 1:",name1[1])
print("Index 2:",name1[2])
print("Index -1:",name1[-1])  #Negative indexing


#Traversing a string using for loop
print("Traversing a sting using for loop:")
for i in name1:
    print(i)


#we can also use list comprehension here
print("Traversing using List comprehension:")
list=[char for char in name1]  #for every char in name1, we are assigning char to the list
for i in list:
    print(i)


#Find length of a string using len() function
print("length of name1:",len(name1))

#find a character or a substring in a string using find function
#find() function gives the index of the 1st occurence of the character, and if the character is not present in the original string it will return -1
print("finding character 'R' at index:",name1.find('R'))
print("finding character 'M' at index:",name1.find('M'))
print("finding substring 'hul' at index:",name1.find('hul'))
