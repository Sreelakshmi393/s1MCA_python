dict1={}
dict2={}

len1=int(input("Enter length of first dict : "))
print("Enter the values of dictionary 1 ")
for i in range(len1):
    k1=int(input("Enter the key values : "))
    v1=input("Enter the values : ")
    dict1[k1]=v1
len2=int(input("Enter length of second dict : "))
print("Enter the values in dictionary 2 ")
for i in range(len2):
    k2=int(input("Enter the key values : "))
    v2=input("Enter the values : ")
    dict2[k2]=v2
dict1.update(dict2)
print(dict1)
