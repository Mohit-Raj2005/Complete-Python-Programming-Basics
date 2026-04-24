def outerFunction():
    x=2   #variable of outer function

    def innerfunction():
        y=5
        sum=x+y
        return sum
    
    return innerfunction()
#output=outerFunction()
print(outerFunction())