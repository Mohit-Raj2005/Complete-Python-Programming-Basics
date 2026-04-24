#creating tuples
colours=("red","yellow","orange")

#creating tuple with one element
fruit=("apple",) # , must be added to make it a tuple otherwise it willo take it as a string
fruit=tuple(("apple"))  #we can also use the keyword tuple directly
#check type of tuple
print(type(fruit))

#check length of the tuple by using len() function
print(len(colours))


#accessing elements of a tuple
print(colours[1])  #this is positive indexing

#negative indexing
print("by using negative indexing element at index -2",colours[-2])

#range indexing to access elements from one index till other
print("printing elements from index 0 to 2:",colours[0:3])
#negative range indexing
print("printing elements from index -3 to -1:",colours[-3:])  #here stopping index is left blank so that it will print all elements till end


#check if any particular item is present in the tuple or not
if "yellow" in colours:
    print("yellow is present ")


#teaversing a tuple
for i in range(3):
    print(colours[i])

#concatinate 2 tuples
morecolours=("blue","black","white","pink")
finalcolour=colours+morecolours
print("final concatinate tuple:",finalcolour)


#unpacking a tuple
#we are creating 3 variable colour1,colour2,colour3 and assigning elements of colours tuple to them
print("unpacking of tuple")
colour1,colour2,colour3=colours
print(colour1,colour2,colour3)

