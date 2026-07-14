# Class is a bluprint of object
#object is a instance of class

class person: #class created
    pass

obj = person() #object created


class student:
    name  = "sachchidanand"
    age = 23
     
obj1 = student()

print(obj1.name)
print(obj1.age)

obj1.nickname = "Milan"
print(obj1.nickname)

obj2 = student()
# print(obj2.nickname)#it will give an error as nick name belongs to obect obj1 only