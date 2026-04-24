list=[10,20,30,40]
list.append(50)  #append() function is used to add an element at the end of a list
print("append() function")
print(list)

#insert() function is used to insert the element in a list at any particular index
print("insert() function")
list.insert(3,100) #100 is inserted in the list at index 3
print(list)

#extend() function is used to insert or append one list at the end of the existing list
list2=["banana","orange","guava","mango"]
list.extend(list2)    # adding list2 at the end of list
print("extend() funcction")
print(list)


#removing elements from a list
#remove() function is used to remove any particular elements from a list
print("remoing elements from the list using remove() function")
list.remove(10)  #removes 10
print("final list",list)

#pop() function is used to remove elements from a list at a particular index and if the index is not mentioned then the last item of list get removed
print("removing element from the list using pop() function")
list.pop(3)  #rewmoves element at index 3 i,e. 40
print(list)


#updating items in a list
print("updating items in a list")
lists=[10,20,30,40,50,70,90,100]
print("before updating",lists)
lists[4]= "RAM"  #updating 50 with RAM
print("after updating",lists)
#updating range of list
lists[2:5]=["P","Q","R"]  # : this must be used 
print("after updating range of list",lists)
