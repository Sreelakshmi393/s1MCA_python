dict1 = {}
dict2 = {}

l1 = int(input("Enter the first limit : "))
for i in range(l1):
    key=input("key : ")
    val=input("Value : ")
    dict1[key]=val

l2 = int(input("Enter the second limit : "))
for i in range(l2):
    key=input("key : ")
    val=input("Value : ")
    dict2[key]=val

print(dict1)
print(dict2)

dict1.update(dict2)
print(dict1)