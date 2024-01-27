n = int(input("Enter step number : "))
num=1
for i in range(1,n+1):
    for j in range(1, i+1):
        print(i*j, end=" ")
    print("\r")
    