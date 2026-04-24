#creating a dictionary
phone={
    "riya":882211,
    "ramu":771100,
    "keshav":660011
}
#printing the dicionary
print(phone)

#checking the type of dictionary
print(type(phone))

#check the length of the dictionary
print("length:",len(phone))

#access items of a dictionary
print("Riya:",phone["riya"])  #this will print the values or number associated with the name in the dictionary

print(phone.get("riya"))  # phone.get also works similar to above code

print(phone.keys()) #this will print all the keys in the dictionary

#we can update the values in the dictionary
print("updating the number of riya in dictionary")
phone["riya"]=220022
print(phone)

#we can add elements in the dictionary
print("adding new element BASHU in the dictionary")
phone["BASHU"]= 4455667788
print(phone)

#we can add new dictionary to the existing dicctionary
morephone={
    "shyam":789456,
    "sohan":987654
}
print("adding new dictionary to existing dictionary")
phone.update(morephone)  #update() function adds this new dictionary to the existing phone dictionary
print(phone)

#removing elementts in the dictionary using pop function
print("removing element from the dictionary using pop function")
phone.pop("riya")
print(phone)

#we can use popitem() funtion to remove the last added item
print("removing last item sohan using popitem function")
phone.popitem()
print(phone)  #sohan gets removed


#we can use clear function and this will clear or empty the dictionary
#phone.clear()
#print(phone)

#printing values of a dictionary
for x in phone:
    print(x)  #this code will print all the keys of the dictionary
for x in phone:
    print(phone[x])  #this will print all the values associated with keys


#we can use phone.items() function to make elements of dictionary a separate items and then print them
print("using phone.items() function:")
for x in phone.items():
    print(x)  

print("printing both separately using two variables:")
for x,y in phone.items():
    print(x,y)  