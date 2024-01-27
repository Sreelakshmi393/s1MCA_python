l1 = []
l2 = []

n1 = int(input("Enter list 1 length : "))
print("Enter the elements of list 1 : ")
for i in range(0,n1):
    num = int(input())
    l1.append(num)

print(l1)

n2 = int(input("Enter list 2 length : "))
print("Enter the elements of list 2 : ")
for i in range(0,n2):
    num = int(input())
    l2.append(num)

print(l2)

if(len(l1)==len(l2)):
    print("Lists are of same length")
else:
    print("Lists are not of same length")

sum1 = 0
sum2 = 0

for i in l1:
    sum1 = sum1+i

for i in l2:
    sum2 = sum2+i

if(sum1 == sum2):
    print("Lists sum to same value")
else:
    print("Lists sum to different value")

for i in l1:
    num1 = i 
    for j in l2:
        num2 = j
        if(i==j):
            print(i, "appears in both lists")
