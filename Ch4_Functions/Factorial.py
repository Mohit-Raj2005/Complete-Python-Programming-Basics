#Factorial for a non-negative integer using function

def factorial(n):
     fact=1
     for i in range (1,n+1):
        fact=fact*i
     return fact

num=int(input("enter the number for factorial:"))
if num>=0:
    Factorial= factorial(num)
    print(f"The factorial of {num} is:",Factorial)
else :
    print("invalid number")