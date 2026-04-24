#for converting characters to uppercaase using upper() function
str1="new york"
print("str1:",str1)
str2=str1.upper()  #upper() function converts string to upper case
print("upper case string:",str2)

#converting to lower case using lower() function
str3=str2.lower()
print("Lower case using lower() function str3:",str3)

#for capitalising the first character of our string using capitalise() function
#n will get capitalise to N
str4=str3.capitalize()
print("capitalising the first character str4:",str4)

#for stripping/removing any trailling whitespaces using strip() function
str1="    Hello World    "
str2=str1.strip()
print("with whitespaces:",str1)
print("stripping white spaces:",str2)

#replacing substring using replace() function,by creating a new string with replaced words
str1="hello world, what a beautiful world it is!"
print("before replace:",str1)
str2=str1.replace("world","Ram",1)
print("after replace:",str2)


#splitting string into list using split() function
fruits="apple banana mango orange guava"
print("before split:",fruits)
print("After split:",fruits.split())

#concatination in a string using "+" operator
str1="hello world "
str2="what a great place it is"
print("str1:",str1)
print("str2:",str2)
print("string concatination:",str1+str2)


#formatting string using format() function
fruit1="apple"
fruit2="mango"
#directly using f 
#print(f"i have {fruit1} and {fruit2}")

#formatting using format() function
str="I have {f1} and {f2}".format(f1=fruit1,f2=fruit2)
print(str)