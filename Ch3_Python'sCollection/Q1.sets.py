#find intersection of three sorted list using sets and taking input from user

n1=int(input("enter the size of list 1:"))
ar1=  []
print("enter the elements of list 1:")
for _ in range(n1):
    a=int(input(""))
    ar1.append(a)

n2=int(input("enter the size of list 2:"))
ar2=  []
print("enter the elements of list 2:")
for _ in range(n2):
    b=int(input(""))
    ar2.append(b)

n3=int(input("enter the size of list 3:"))
ar3=  []
print("enter the elements of list 3:")
for _ in range(n3):
    c=int(input(""))
    ar3.append(c)

#typecasting lists into sets
s1=set(ar1)
s2=set(ar2)
s3=set(ar3)
print("s1:",s1,"s2:",s2,"s3:",s3)
#joining using intersection update
s1.intersection_update(s2)
s1.intersection_update(s3)
print("intersection of s1,s2 and s3:",s1)