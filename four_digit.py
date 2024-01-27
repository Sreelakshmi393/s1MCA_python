"""def even(i):

    if(i>0):
        num=i%10
        new_num=i/10
        if(num%2 == 0):
            even(new_num)
            return i
        
def perfect(i):
    rt = i**0.005
    if(rt*rt == i):
        return i
    
     

#n = int(input("Enter the number : "))
list = []
for i in range(1000, 10000):
    if even(i) and perfect(i):
        list.append(i)

print(list)"""

def is_perfect_square(number):
    root = int(number ** 0.5)
    return root * root == number

def has_all_even_digits(number):
    digits = [int(digit) for digit in str(number)]
    return all(digit % 2 == 0 for digit in digits)

# Iterate through four-digit numbers
for i in range(1000, 10000):
    if has_all_even_digits(i) and is_perfect_square(i):
        print("Perfect square with all even digits:", i)
        break
