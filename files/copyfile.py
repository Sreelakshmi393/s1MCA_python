f = open("new.txt", 'r')
nf = open("newfile.txt", 'w')
nf1 = open("newfile.txt", 'a')
lines = f.read()
# print("Original file : ")
# for i in range(0,len(lines)):
#     print(lines[i], end = " ")
#     if i%2 != 0:
#         nf.write(lines[i])
    
# nf.close()
# f.close()

# print("New file : ")
# f = open("newfile.txt", 'r')
# lines = f.read()

# for i in range(0, len(lines)):
#     print(lines[i], end=" ")
"""l=lines.split("\n")
print(l)

count=1

for i in l:
    if count%2!=0:
        nf.writelines(i)
    count+=1"""

count = 0
for line in f:
    count+=1
    if count%2!=0:
        nf1.write(line)
    