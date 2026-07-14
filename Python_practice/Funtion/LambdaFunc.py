# lambda function is also called anonymous function
# It can take any number of argument
# it can have single line expression

func = lambda x : x+10
print(func(6))

add = lambda a,b : a+b
print(add(3,5))

# lambda inside a function 
def myfunc():
    #return a new function
    return(lambda msg : print(msg))
myfunc()("Hello world")