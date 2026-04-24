#pass by value

def addOne(n):
    n=n+1
    print("inside funtion the variable:",n)

x=5    #any change made inside the function does not affect the original value of the variable
addOne(x)
print("outside function the variable:",x)

#pass by reference

def modifyList(lst):
    lst.append(4)
    print("inside function:",lst)

list=[1,2,3]     #any changes mafe inside the function affects the original value of the list
modifyList(list)
print("outside function:",list)