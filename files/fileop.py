##f = open("new.txt")
##print(f.read())


def read_file(f1):
    list=[]
    with open(f1,'r') as file:
        for line in file:
            list.append(line.strip())
    return list

f1 = "new.txt"
list1 = read_file(f1)
print("Lines are :")
for line in list1:
    print(line)