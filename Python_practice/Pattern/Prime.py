# num = int(input("Enter the number: "))
# count = 0
# factors = []

# for i in range(1,num+1):
#     if num<=0: 
#         print("Enter the valid Number: ")
#     elif num%i == 0:
#             count += 1
#             factors.append(i)
# print("The number of factors is: ",count)
# print(factors)
# if factors == [1,num]:
#     print("prime")
# else:
#     print("Not Prime")
    
    
fact = 0
num = int(input("Enter the number to check prime or not: "))
for i in range(1,num+1):
    if num%i == 0:
        fact = fact+1
        if fact>2:
            print("Not a Prime Number")
            break
else:
    print("prime Number")