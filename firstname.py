list = ["sam", "ram", "arjun", "amritha", "akhi"]

count = 0
for i in list:
    name = i
    for j in name:
        if(j=="a"):
            count=count+1

print(count)