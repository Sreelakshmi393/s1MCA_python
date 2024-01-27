str = input("Enter the string : ")
l = len(str)

first = str[0]
last = str[l-1]

mod_str = last+str[1:l-1]+first
print(mod_str)