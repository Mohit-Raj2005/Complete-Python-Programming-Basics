#n = (int(input("enter the number:")))
#sum=0
#for i in range (1,n+1):
 #   sum = sum+i
#print(f"sum of first{n} numbers is",sum)

#writing a function for calculating sum from 1 to n

def sumOneToN(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum  

n1 = (int(input("enter the number:")))
output=sumOneToN(n1)
print(f"the sum of first {n1} natural numbers:",output)

n2 = (int(input("enter the number:")))
output=sumOneToN(n2)
print(f"the sum of first {n2} natural numbers:",output)