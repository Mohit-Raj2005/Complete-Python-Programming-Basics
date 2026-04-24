#here we are creating a tuple and assigning each element into a list using for loop and then typecasting that into tuple and printing it
inputtuple=(1,2,3,4,5)
print("input tuple",inputtuple)
list = []
#adding reversed values in a list
for x in reversed(inputtuple):
    list.append(x)
#typecasting list into tuple
outputtuple=tuple(list)
print("reversed tuple:",outputtuple) 