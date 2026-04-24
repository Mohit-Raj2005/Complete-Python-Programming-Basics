#Make a function which calculate Fibonacci sequence using Recursion

def fibonacci(n):
    if n==1:    #base case
        return 0
    elif n==2:   #base case
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)        #recursive case
    

num=int(input("Enter a number for fibonacci series:"))
for i in range(1,num+1):
    print(fibonacci(i))