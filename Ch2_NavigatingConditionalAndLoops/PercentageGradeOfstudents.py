#yaha pe &(bitwise and )ke jagah LOGICAL and ka use karna hai
#yaha pe & ye nahi "and" hoga

percentage=int(input("enter the marks percentage:"))
#if percentage is between 100 and 81
if(percentage>=81 and percentage<=100):
    print("VERY GOOD")
#if percentage is between 61 and 80
elif(percentage>=61 and percentage<=80):
    print("GOOD")
#if percentage is between 60 and 41
elif(percentage>=41 and  percentage<=60):
    print("AVERAGE")
#if percentage is below 40
elif(percentage<=40 and percentage>=0):
    print("FAIL")
else:
    print("invalid percentage")
