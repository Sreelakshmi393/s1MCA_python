a,b = map(int, input("Enter the numbers : ").split())
c,d= a,b
while(b):
    a,b=b,a%b
print("GCD of ", c , " and ", d ," is ", a)