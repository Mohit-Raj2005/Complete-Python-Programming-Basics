#taking cost price and selling price as input 
#then we are calculating net profit and loss
#then printing the loss or profit made
cp=float(input("enter the cost price of the item:"))
sp=float(input("enter the selling price of the item:"))
net=sp-cp
if (net>0):
    print("the profit made is:",net)
elif (net<0):
    print("the loss made is:",net)
else:
    print("no profit and no loss")