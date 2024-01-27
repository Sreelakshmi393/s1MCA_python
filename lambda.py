a = int(input("Enter side of sqaure : "))
sq = lambda a : a*a
print(sq(a))

l,b = map(int, input("Enter length and breadth : ").split())
rec = lambda l,b : a*(l+b)
print(rec(l,b))

b,h = map(int, input("Enter breadth and height : ").split())
tri = lambda b,h : 0.5*b*h
print(tri(b,h))
