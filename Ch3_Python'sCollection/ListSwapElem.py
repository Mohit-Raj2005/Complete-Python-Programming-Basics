n=int(input("enter the sizer of the list:"))

list= []
for _ in range(n):
    num=int(input("enter the element of list"))
    list.append(num)

idx1=int(input("enter index1:"))
idx2=int(input("enter index2:"))
print("before swapping:",list)

#swapping values at index 
temp=list[idx1]
list[idx1]=list[idx2]
list[idx2]=temp
print("after swap final list:",list)