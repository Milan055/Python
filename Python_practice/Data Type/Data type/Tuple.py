#Odered,Sequence can store diffrent type of data 
#Immutable

tuple1 =(3,4,5,6,2,1)
print(tuple1)
print(type(tuple1))

# List can be converted in tuple using tuple constructor or we can say that a tuple
# can be created by a list using tuple caonstructor

T1 = tuple([1,2,3,4])
print(T1)

T2 = tuple("Sachchidanand")
T3 = tuple(tuple1)
print(T2,T3)

#Tuple with Single Element
 
T =(1,) #we must put a comma other wiseit will be considered as a int
print(type(T))


#Methods in tuple
# 1 Count() Method

Fruits = ('Mango','Apple','Banana','Guava','Strawberry','Apple','Mango')
print(Fruits.count('Jack'))

#2 Index() use to find indexnumber
print(Fruits.index("Strawberry"))


print(Fruits[1:])
print(Fruits[-3])

# Fruits[3] ="Aam" it is not suported as it is immutbale

print(Fruits[2:4])