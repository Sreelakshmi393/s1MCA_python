s = input("Enter the string : ")
print("Original string : ", s)
if s.endswith('ing'):
    s1=s[:-3]
    s1+='ly'
else:
    
    s1=s+'ing'
print("After insertion : ",s1)
print(s1)