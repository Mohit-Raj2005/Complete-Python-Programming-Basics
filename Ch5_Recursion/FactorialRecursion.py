#Factorial of a number using Recursion

def factorial(n):
    if n==0:
       return 1
    Fact=n*factorial(n-1)
    return Fact

num=int(input("Enter the number for factorial:"))
if num>=0:
    Factorial=factorial(num)
    print(f"The factorial of {num} is:",Factorial)
else:
    print("Invalid number")