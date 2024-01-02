a, b, c = map(int, input("Enter three numbers : ").split())
if(a>b):
    if(a>c):
      print("The largest is ",a)
    else:
      print("The largets is ",c)
elif(b>c):
   print("The largest is ",b)
else:
   print("The largest is ",c)