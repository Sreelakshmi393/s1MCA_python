list = input("Enter strings : ").split()

max_length = 0
for i in list:
    if(len(i)>max_length):
        max_length = len(i)

print(max_length)