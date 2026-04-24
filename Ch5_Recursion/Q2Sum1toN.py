#write a program to print sum from 1 to n
def sum(n):
    sum=0
    for i in range (1,n+1):
        sum=sum+i
    return sum

num=int(input("Enter a  number for sum:"))
output=sum(num)
print(f"The sum of numbers from 1 to {num} is:",output)