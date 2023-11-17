list1 = []
list2 = []
sum1=0
sum2=0

n1 = int(input("Enter the length of list 1 : "))
print("Enter the elements of list 1 ")
for i in range(0,n1):
    ele = int(input())
    sum1=sum1+ele
    list1.append(ele)
print(list1)

n2 = int(input("Enter the length of list 2 : "))
print("Enter the elements of list 2 ")
for i in range(0,n2):
    ele = int(input())
    sum2=sum2+ele
    list2.append(ele)
print(list2)

if(len(list1)==len(list2)):
    print("The two lists are of same length")
else:
    print("The two lists are not of same length")

if(sum1==sum2):
    print("Two lists sums to same value")
else:
    print("Two lists doesn't sums to same value")

out = set(list1).intersection(list2)
if out:
    print("Lists contains common value")
else:
    print("Lists dosen't contains common value")

