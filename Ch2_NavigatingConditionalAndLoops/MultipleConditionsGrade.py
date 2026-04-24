eng=int(input("Enter the english marks:" ))
maths=int(input("Enter the maths marks:" ))
if eng>=80 and maths>=80:
    print("A grade ")
elif eng>=80 or maths>=80:
    print("B grade")
else:
    print("C grade")