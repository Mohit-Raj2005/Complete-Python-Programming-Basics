#write a program to print numbers from n to 1

def num(n):
    if n==0:
        return 
    
    num(n-1)     #Recursive Case
    print(n) 
m=int(input("enter the number"))
num(m)

