#given  a string and a number , we need to mirror the characters from the Nth position upto the length of the string in alphabetical order. in mirror operation,we change 'a' to 'z', 'b' to 'y' and so on
#input: N=3
# paradox
#output= paizwlc
inputstring=input("enter a string:")
n= int(input("enter n:"))


#creating dictionary for mirror operation
alphabets="abcdefghijklmnopqrstuvwxyz"
reversealphabets=alphabets[::-1]  #this will reverse the string and store in rverse variable

dict1= dict(zip(alphabets,reversealphabets))

#finding the part of string on which we will do mirror operation
prefix=inputstring[0:n-1]
suffix=inputstring[n-1:]

#finding the mirror string
mirror= ""
for i in range(len(suffix)):
    mirror=mirror+dict1[suffix[i]]

#creating the final string
res=prefix+mirror
print("mirrored:",res)