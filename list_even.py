a=list(map(int, input("Enter the elements in the list : ").split()))
print("Original list is : ",a)
b=[i for i in a if i%2!=0]
print("Final list : ",b)
