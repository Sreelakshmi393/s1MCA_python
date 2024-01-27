curr = int(input("Enter current year : "))
lim = int(input("Enter year limit : "))

for i in range(curr, lim+1):
    if(i % 400 == 0) or (i % 4 == 0 and i % 100 != 0):
        print(i, " ")