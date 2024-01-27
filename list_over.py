list = []

n = int(input("Enter the limit : "))
print("Enter the elements ")
for i in range(0, n+1):
    num = int(input())
    if(num > 100):
        list.append("over")
    else:
        list.append(num)
print(list)