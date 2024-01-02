s = input("Enter a word : ")
c={}
for i in s:
    if i in c:
        c[i]+=1
    else:
        c[i]=1

print("Characters\t \tNo of occurence")
for i in c:
    print(i, "\t\t\t", c[i])