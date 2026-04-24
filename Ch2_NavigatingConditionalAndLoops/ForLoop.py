#without step of increase... it will by default increase the variable by 1
print("without increasing step")
for i in range(1,12):
    print(i,"RADHE RADHE \n")

#with step of increase
print("with 2 as increasing step")
for i in range(1,12,2):
    print(i,"RADHE RADHE \n")

#if we dont initialise the i variable, it will by default start from 0
print("without initialising the variable")
for i in range(12):
    print(i,"RADHE RADHE \n")

#without defining the looping variable
print("without declaring the looping variable")
for _ in range(12):
    print("RADHE RADHE")