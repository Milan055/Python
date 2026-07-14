def Greet(Name,Message="How are you"): #default Argument
    print(Name,Message)

Greet("Sachchidanand Chaudhary","Hi") #Agar hi likhna bhul gya to how are you print hoga

def Greet(Name,age,Message): 
    print(Name,age,Message)
Greet("Sachchidanand",23,"Good Mornig")
Greet(Name="Sachchidanand",Message="Good Mornig",age=23) #keyword argument keyword laagne se order matter 
                                                        #print order mei hi hoga

# positional arguments
def add(x,y):
    print("x ",x)
    print("y ",y)
    print(x+y)
add(6,5)


#when there are number of variable to do a single task
def add(*args): #yha args ki jagah kuch bhi le sakte hai
    print(args)
    sum =0
    for num in args:
        sum = sum+num
    return sum
print(add(2,3,4,5))
    