class student:
    #initialize/constructor for objects
    def __init__(self,name,age): #here self represent the object that expect to be created self is just a key word we can put any word insted of self
        self.name = name
        self.age = age
obj1 = student("Sachchidanad",23)
obj2 = student("milan",24)
print(obj1.name)
print(obj2.name)


class person:
    def __init__(self,name,age="34",hobby="footboll"):# Now age and hobby become optional parameter 
        self.name = name
        self.age = age
        self.hobby = hobby
obj1 = person("Sachchidanand",23,"Cricket")
obj2 = person("milan",24)
obj3 = person("anand")
print(obj1.hobby)
print(obj3.hobby)


class person:
    country = "India" #this is called class atribute or class variable this will not chnage object to object 
    def __init__(self,name,age):
        self.name =name # this is instace will change according to object to object
        self.age = age #this is also a instance will change acc to obj
obj1 = person("Sachchidanand",23)
obj2 = person("Milan",24)
print(obj1.name,obj1.country)
print(obj2.name,obj2.country)
print(person.country)#we do nit need any object to call a class  variable