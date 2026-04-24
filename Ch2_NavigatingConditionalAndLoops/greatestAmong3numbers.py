#program to check greatest among three numbers
a=int(input("enter the first number a:"))
b=int(input("enter the second number b:"))
c=int(input("enter the third number c:"))
#if a is greatest
if a>b and a>c:
    print("a is greates")
#if b is greatest
elif b>a and b>c:
    print("b is greatest")
#if c is greatest
elif c>a and c>b:
    print("c is greatest")
#if all the numbers are equal
else:
    print("all numbers are equal")
