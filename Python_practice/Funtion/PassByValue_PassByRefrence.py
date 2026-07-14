# pass by value 
# in this changes occur only in copy of data not in original data
# it happens only in un-mutable data like integer,string,tuple

num = 6
def modify_num(a):
    a = a+1
    print(a)
   
print("Number before modifying: ",num)
modify_num(num)
print("Number after modifying: ",num)

#Call by refrence in this canges occur in original data
#CAll by ref takes palces in mutable data type ex list,dictionary

L1 = [1,2,3,4]
def modifiy_list(li):
    li.append(5)
    print(li)
print("list before mod: ",L1)

modifiy_list(L1)

print("list After mod: ",L1)
    