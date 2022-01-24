def sayHello(name):
    print("hello " + name)

def askName():
    name = input("enter name: ")
    return name

n = askName()
sayHello(n)
