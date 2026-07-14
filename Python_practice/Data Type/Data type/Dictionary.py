# Dictionary Store Data in from of key value Pair Dictionary(Key,Value)
# It is Unodered
# It is Mutable
# Key should be unique and immutable
# It can store Hetrogenious Data

Students_Details = {
    'Name':'Sachchidanand',
    'Age':'25',
    'City':'Varanasi'}
print(Students_Details)
print(type(Students_Details))

# Methods in dictionary
#Dictionary Constructor Method dict{} in this key must be a string

dict1 = dict(a='Sachchidanand',b='Milan',c="Chaudhary")
print(dict1)

#Accessing the elements of the dictionary

print(Students_Details['Name'])

#Accesing all key using Key() method

print(Students_Details.keys())
print(Students_Details.values())
print(Students_Details.items())


#Adding Element in the dictonary Method 1
Students_Details['Country']='India'
print(Students_Details)
#Method 2
Marks_Details = {'English':100,'Mathematics':90,'Science':99}
Students_Details.update(Marks_Details)
print(Students_Details)

#Pop() method
print(Students_Details.pop('City'))
print(Students_Details)
#del Keyword

del Students_Details['Age'] #del is a statment or a keyword not a method or a function
print(Students_Details)

#Clear() method
Students_Details.clear()
print(Students_Details)