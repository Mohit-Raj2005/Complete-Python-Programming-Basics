fruits=["apple","banana","mango","orange"] #create a list
print(fruits)  #print a list
print(type(fruits)) #check type of list
print(len(fruits))  #len() function gives us the length of the list

#checking if any item is present in the list
if "banana" in fruits:
    print("banana is in the list of fruits")

if "kiwi" not in fruits:  #checking is any item is not preseent in the list
    print("kiwi is not present in the list of fruits")

#inde4xing in list
print("element in list at index 1 is ",fruits[1])   #banana
print("element in fruit list at inedx -3 is:",fruits[-3])  #banana
print("elements of list from index 1 to 2 is:",fruits[1:3]) #banana and mango and (:) is used in this
print("elements of list from index -3 to -1 is:",fruits[-3:-1])  #banana and mango
