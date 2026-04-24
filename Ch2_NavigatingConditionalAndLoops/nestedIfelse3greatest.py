#program to check greatest among three numbers using nested if else
#using nested if else
a=int(input("enter the first number a:"))
b=int(input("enter the second number b:"))
c=int(input("enter the third number c:"))
if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("c is greatest")
else:
    if b>c:
        print("b is greatest")
    else:
        print("c is greatest")