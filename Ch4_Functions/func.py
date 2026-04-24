#write a functtion that prints hello world

def helloWorld():
    print("HELLO WORLD!!!!")    #body of the function

helloWorld()

#add function
def add(n1,n2):
    sum=n1+n2
    return sum

#positional argument
print("positional argument sum is:" ,add(3,5))

#keyword argument (named argument)
print("Named argument sum:",add(n1=5,n2=5))

#default argument
def add(n1,n2=2):  #here n2 will take default argument as "2"
    sum=n1+n2
    return sum
print("Default argument sum:",add(5))

#Arbitrary arguments
print("arbitrary arguments")

def addAllnumbers(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
output=addAllnumbers(2,3,4,5)  #all arguments will be taken as tuple
print("arbitrary arguments sum:",output)

#*kwargs (keyword arguments)
print("*kwargs Keyword arguments") #variable length arguments that will take arguments as key value pairs or Dictionary

def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)

studentInfo(name="Ram",age=22,city="Ayodhya")
studentInfo(name="Rhul",age=25,city="Delhi")