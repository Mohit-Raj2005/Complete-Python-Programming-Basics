#string
name = "ramu"

#integer
rollnumber = 25

#float
percentage = 95.5

#boolean data type
is_student = True

print(name, rollnumber, percentage, is_student)

percentage = 94.0
print(name, rollnumber, percentage, is_student)
print(type(name))
print(type(rollnumber))
print(type(is_student))

print("my name is "+ name + f" my rollnumber is {rollnumber}" + " my percentage is",percentage)

#we can print expressions also
print("my percentage is now ",percentage - 1.0)

#we can also print with a separator
print(name, rollnumber, is_student, percentage, sep="-")
x = 1
y = 2
z = 3 
m = 4 
print(x, y, z, m, sep="->")