dict1={}
len=int(input("enter the limit:"))
for i in range(len):
		salary=input("Enter salary : ")
		name=input("ENTER THE NAME:")
		dict1[salary] = name
print("ascending dict:")
ascending=dict(sorted(dict1.items()))
print(ascending)
print("descending dict:")
descending=dict(sorted(dict1.items(),reverse=True))
print(descending)
