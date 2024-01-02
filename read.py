from Graphics import rectangle
from Graphics.circle import *
from Graphics.graphics3d.cuboid import area as a, peri as p
from Graphics.graphics3d import sphere

l = int(input("Enter the length of rec :"))
b = int(input("Enter the breadth of rec :"))
rectangle.area(l,b)
rectangle.peri(l,b)
print("\n")

r = int(input("Enter the radius of circle :"))
area(r)
peri(r)
print("\n")

r=int(input("Enter the radius of sphere : "))
sphere.area(r)
sphere.peri(r)
print("\n")

l = int(input("Enter the length of cuboid :"))
b = int(input("Enter the breadth of cuboid :"))
h = int(input("Enter the height of cuboid : "))
a(l,b,h)
p(l,b,h)
