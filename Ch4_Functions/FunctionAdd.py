#function that takes two numbers as input and return their sum

def add(n1,n2):
    sum=n1+n2
    return sum

x=int(input("enter the 1st number:"))
y=int(input("enter the 2nd number:"))
print("the sum is ",add(x,y))