n1 = int(input("First number : "))
n2 = int(input("Second number : "))
n3 = int(input("Third number : "))

if(n1>n2):
    if(n1>n3):
        print("Largest is ",n1)
    else:
        print("Largest is ",n3)
elif(n2>n3):
    print("Largest is ",n2)
else:
    print("Largest is ", n3)