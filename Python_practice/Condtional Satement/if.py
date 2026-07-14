Marks =int(input("Enter the marks: "))
if Marks>90:
    print("A")
elif Marks>=75 and Marks <90:
    print("B")
elif Marks>=50 and Marks <75:
    print("C")
else:
    print("D")

if Marks:
    print("inside If")
else:
    print("Inside else")