def factors(n):
    for i in range(n, 0, -1):
        if(n%i == 0):
            print(i)

n = int(input("Enter the number"))
factors(n)