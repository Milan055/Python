# method overloading means multiple methods with same name

class calculator():
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
obj1 = calculator()
obj2 = calculator()
print(obj1.add(5,6,7))
print(obj2.add(6,7))