newfile = open("newfile.txt", 'w')

file1 = open("new.txt",'r')
file2 = open("newfile.txt",'a')

count = 0
for line in file1:
    count+=1
    if(count%2 != 0):
        file2.write(line)

file1.close()
file2.close()

f = open("newfile.txt")

for line in f:
    print(line)
