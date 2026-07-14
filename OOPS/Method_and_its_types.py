# Instance method/object method
# class method 
# static method

#1 instance method/object method

class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def findage(self):
        return self.age
per = person("sachchidanand",100)
print(per.findage())


#2 class method

class person():
    country = "India"
    
    @classmethod #decorator(meta data)
    def greet(cls): #this is class method
        print("Hello from the class",cls.country) #this have the acess of class property but acess to obj property
        
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def findage(self):
        return self.age
    
per = person("sachchidanand",100)
print(per.findage())
person.greet()
per.greet()

#3 static method

class person():
    country = "India"
    
    @classmethod #decorator(meta data)
    def greet(cls): #this is class method
        print("Hello from the class",cls.country) #this have the acess of class property but acess to obj property
        
    @staticmethod    
    def hello():
        print("Hello")#It have neither access of class nor object
        
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def findage(self):
        return self.age
    
per = person("sachchidanand",100)
print(per.findage())
person.greet()
per.greet()
person.hello()