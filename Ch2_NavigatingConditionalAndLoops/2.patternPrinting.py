#printing digits in triangle form
m=int(input("entr the number of rows for triangle form:"))
for i in range(1,m+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
