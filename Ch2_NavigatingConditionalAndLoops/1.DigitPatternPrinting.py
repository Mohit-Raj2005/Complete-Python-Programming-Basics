#printing digits in horizontal rows

n=int(input("enter the number of rows for horizontal form5:"))
for i in range(n): #loop for rows
    for j in range(1,n+1):
        print(j,end=" ")
    print("") #empty print so that after printing one row it goes to the next line 



