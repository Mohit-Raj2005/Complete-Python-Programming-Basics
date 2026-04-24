#digit printing in pascals triangle form by printing few spaces in the front
n=int(input("enter the value of n:"))
for i in range(1,n+1): #loop for rows
    print(" " * (n-i),end="")  #printing spaces
    #printing digits
    for j in range(1,(2*i)):
        print(j,end="")
    print()