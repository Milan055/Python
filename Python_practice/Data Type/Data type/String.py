#string is sequnce or group of characers
#String is Immutable
#as string is immutable it saves spaces 
Name = "SAchchidanand Chaudhary"
city = "Varanasi"
Country  = "India"

# #String is Immutable
# str ="Milan"
# str[0] = 'x'
# print(str) #will throw error



#as string is immutable it saves spaces as is stores adress for same pice of data
str1 ="Milan"
str2 ="Milan"
print(id(str1),id(str2)) #adress is same

#Accesing element by index Number

print(Name[3:8])
print(Name[14])


#Concatatanation operator

First_name = "Sachchidanand"
Last_name = "Chaudhary"
Full_name = First_name +" "+ Last_name
print(Full_name)

#Length Method
print(len(Full_name))

#String Slicing same apply for list and tuple also
Str ="Sachchidanand Chaudhary"
print(Str[0:14])
print(Str[1:]) #it will go till last
print(Str[:14]) #begining to 13th indext
print(Str[:])#it will print entire string
print(Str[-23:-9])
print(Str[-13:13])

#upper(),Lower() and Capitalize() method
print(Str.upper())
print(Str.lower())
Str2 = "miLaN"
print(Str2.capitalize())

#Replace Method

Str = "Hello Every One,I am very good ,I am nice,I am wow"
print(Str.replace("I am","We are"))