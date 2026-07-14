# F_num= 1
# S_num = 1
# T_num = 0
# print(F_num,end=",")
# for i in range(7):
#     T_num = F_num+S_num
#     F_num = S_num
#     S_num =T_num
#     print(F_num,end=",")

# num =int(input("Enter the number upto which you want to print: "))
# F_num= 1
# S_num = 1
# # print(F_num,end=",")

# if num<=0:
#      print("Enter Valid Number")
# elif num >=1:
#     print("1",end="  ")
#     for i in range(num):
#         S_num = F_num+S_num
#         F_num = S_num-F_num
#         print(F_num,end=" ")
num = int(input("Enter the number: "))
S_num=1
F_num=1
if num<=0:
    print("Enter the valid number: ")
else:
    for i in range(num):      
        S_num = F_num+S_num
        F_num = S_num-F_num
        print(F_num,end=",")
            


    