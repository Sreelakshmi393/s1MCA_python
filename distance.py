class Distance:
    def __init__(self,km):
        self.__kilometer = km

    def __add__(self,other):
        dist = self.__kilometer+other.__kilometer
        return Distance(dist)

    def __str__(self):
        return f"{self.__kilometer}"
    
obj1 = Distance(23)
obj2 = Distance(32)
d = obj1 + obj2
print(d)