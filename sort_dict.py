dict1={}
len=int(input("Enter the limit : "))
for i in range(len):
    salary=int(input("Enter salary : "))
    name=input("Enter name : ")
    dict1[salary]=name
print("Ascending order : ")
ascending=dict(sorted(dict1.items()))
print(ascending)
print("Descending order : ")
descending=dict(sorted(dict1.items(), reverse=True))
print(descending)