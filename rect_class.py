class Rectangle:
	def __init__(self, length, breadth):
		self.length=length
		self.breadth=breadth
		
	def area(ar):
		area=ar.length*ar.breadth
		print("Area : ",area)
		return area
		
	def peri(pe):
		peri=2*(pe.length+pe.breadth)
		print("Perimeter : ", peri)
		
		
l1 = int(input("Enter the length of first rectangle : "))
b1 = int(input("Enter the breadth of first rectangle : "))
r1 = Rectangle(l1,b1)
a1 = r1.area()
r1.peri()

l2 = int(input("Enter the length of second rectangle : "))
b2 = int(input("Enter the length of second rectangle : "))
r2 = Rectangle(l2,b2)
a2 = r2.area()
r2.peri()

if a1>a2:
	print("Rectangle 1 has largest area")
else:
	print("Rectangle 2 has the largest area")




