#write a python function that checks if the given string is a palindrome or not
def palindrome():
    str=input("enter a string:")
    str2=(str[::-1])   #assigning the str to str2 using concept of slicing with no starting and ending but "-1" as step and this will traverse the str in reverse order
    if str==str2:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")

palindrome()





