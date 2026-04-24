num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))
operator=input("enter ther operation to perform +,-,/,*:")
match operator:
    case "+":
        print("sum is ",num1 + num2)
    case "-":
        print("the difference is ", num1-num2)
    case "/":
        print("the division quotient is ",num1/num2)
    case "*":
        print("the product is ", num1*num2)
    case _:
        print("invalid Operator")