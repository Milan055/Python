Students = ["Yash","Rohan","Ramesh","Suresh","Mahesh"]  #list
print(Students)  
print(type(Students))

List2= list(Students) #construtor method
print(List2)  # Output: ['Yash', 'Rohan', 'Ramesh', 'Suresh', 'Mahesh']


list3 =list("Sachchidanand")
print(list3)

#we can access list element by there index number
L1 = [1,3,5,7,9,4]
print(L1[3]) # positive index 0 to length -1
print(L1[-4]) # Negative index -length to -1

#Inserting or adding element to the list

#Method 1 at the end of list by append()
arr = [3,2,45,5,6,7]
arr.append(12)
print(arr)

#Method 2 at a specific Index by insert() method
arr = [3,2,45,5,6,7]
arr.insert(3,66)
print(arr)

#Method 3 making a list with another list by Extend() method
L1 =[1,3,44]
L2 = ["king","kohli"]
L1.extend(L2)
print(L1)


#Remove Elements from the list 

#Method 1 by Remove Method() it will remove first occurance not all
arr =[2,3,4,2,5]
arr.remove(2)
print(arr)

#Method 2 pop() By default it remove the last element and if we provide index number it will remove that
arr =[2,3,4,2,5]
arr.pop()
print(arr)

#Replacing of value

#Replace value at a given index
Students =['a', 'b', 'c', 'd','e','f']
Students[3] = 'z'
print(Students)

Students[1:4] = 'm','n','o'
print(Students)

#Reverse
Students.reverse()
print(Students)

#Copy() Method
L1 =[1,3,6,44,5,33]
L1_Copy =L1.copy()
print(L1_Copy)
print(id(L1_Copy),id(L1)) #it creates two object fro same data it 

#Sort() method
L1.sort()
print(L1)