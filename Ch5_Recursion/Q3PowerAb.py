#Make a function which calculates 'a' raise to power 'b' using Reccursion
def power(a,b):
   if b==0:
    return 1
   product= a * power(a,b-1)
   return product

num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
output=power(num1,num2)
print(f"{num1} raised to power {num2} is:",output)