# No duplicate  Values are Allowed
# Is can stores hetrogeneous data
# Un-odered
# Mutable

#Defining Set
My_set ={1,2,4}
print(type(My_set))
print(My_set)

#Unique Values/No Duplicate and it returns data in sorted Mannner
S1= {1,2,3,4,2,1,3,8,0,43,0,9,9}
print(S1)

#Making Set by Constructor method
S2 =set()
print(S2)

S3 = set({5,6,7})
print(S3)

# add() Method
# Set is Un-odered
S4 = set()
S4.add(1)
S4.add(3)
S4.add(4)
S4.add(5)
S4.add(0)
print(S4)

#discard() Method

S5 = {1,2,3,4,5,6}
print(S5.discard(3))
print(S5)



#Frozenset() method which make set mutable to immutable

fs= frozenset({1,2,3,4,5,3})
print(type(fs))
print(fs)

fs2 = frozenset({45,6,6,4,7})
dict1 = {fs2 : "Vishwa"}
print(dict1)