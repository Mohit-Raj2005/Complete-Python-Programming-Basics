num=int(input("enter the number to check the divisibility by 3 and 5:"))
#checking whether it is divisible by 15
if num%15==0:
    print(num," is divisible by 15")
else:
#checking whether is divisible by 5 or 3
   if num%3==0 or num%5==0:
    print(num," is not divisible by 15 but divisible by 3 or 5")
   else:
      print("it is neither divisible by 3 or 5")