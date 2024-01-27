str = input("Enter a string : ")

first = str[0]
mod_str = first+str[1:].replace(first, '$')

print(mod_str)