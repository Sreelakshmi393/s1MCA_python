str = input("Enter the string : ")
s = str.split()
d={}
for word in s:
    if word in d:
        d[word]+=1
    else:
        d[word]=1
    
print(d)