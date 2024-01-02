num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
a = input("Enter an expression : ")
if('+' in a):
    print("Sum = ",num1+num2)
elif('-' in a):
    print("Difference = ", num1-num2)
elif('*' in a):
    print("Product = ",num1*num2)
elif('/' in a):
    print("Quoitent = :", num1/num2)
elif('%' in a):
    print("Remainder = ", num1%num2)
else:
    print("Invalid operator")
