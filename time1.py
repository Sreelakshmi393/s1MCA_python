class Time:
    def __init__(self,h,m,s):
        self.__hour = h
        self.__min = m
        self.__sec =s
    def __add__(self,a):
        h = self.__hour+a.__hour
        m = self.__min+a.__min
        s = self.__sec+a.__sec
        if(s>=60):
            s%=60
            m+=1
        if(m>=60):
            m%=60
            h+=1
        return Time(h, m, s)
        
    def __str__(self):
        return f"{self.__hour:02d}:{self.__min:02d}:{self.__sec:02d}"
     


x,y,z = map(int, input("Enter the time 1 in format (hh:mm:ss) : ").split(":"))
a=Time(x,y,z)
x,y,z = map(int, input("Enter the time 1 in format (hh:mm:ss) : ").split(":"))
b=Time(x,y,z)
print("Time 1 + Time 2 = ")
print(a+b)
