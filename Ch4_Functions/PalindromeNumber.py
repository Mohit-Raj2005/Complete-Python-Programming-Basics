#write a function to check if the number is palindrone or not

def palindrome(n):
    b=n
    sum=0
    while n>0:
        a=n%10
        sum=sum*10+a
        n=n//10
    if b==sum:
        print("palindrome")
    else:
        print("not a palindrome")
num=int(input("enter a number:"))
palindrome(num)
