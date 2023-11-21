color_list1 = []
color_list2 = []

n1 = int(input("Enter the length of first list : "))
print("Enter the colors for list 1 : ")
for i in range(0,n1):
    color = input()
    color_list1.append(color)

n2 = int(input("Enter the length of list 2 : "))
print("Enter the colors for list 2 :")
for i in range(0,n2):
    color = input()
    color_list2.append(color)

print(set(color_list1).difference(color_list2))