#given a dictionary in python, write a program to find the sum of all the items in the dictionary
dict={
    "a":100,
    "b":200,
    "c":300
}
#values() function gives us directly the values of the elements of the dictionary
#and we can use sum() function to directly add the values of the dictionaries
print("the sum of dictionaries values is:",sum(dict.values()))