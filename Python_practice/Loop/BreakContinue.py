# They are use  to control the flow of loop

for i in range(1,10):
    if(i%4==0):
        break
    print(i)

# for i in range(1,10):
#     if(i%4==0):
#         continue
#     print(i)

for i in range(1,10):
    if(i%4!=0):
        continue
    print(i)
