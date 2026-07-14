def outer():
    print("Helllo from outer")
    
    def inner():
        print("Hello from inner")
    return inner
fn =outer()
fn()

outer()()