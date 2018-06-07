#In Python, a variable declared outside of the function or in global scope is known as global variable.
# This means, global variable can be accessed inside or outside of the function.
x = "global"

def foo():
    print("x inside :", x)

foo()
print("x outside:", x)

x = "global"

#Python treats x as a local variable and x is also not defined inside foo()
def foo2():
    #x = x * 2
    print(x)
foo2()

#Accessing a variable outside of a function generates error
#The output shows an error, because we are trying to access a local variable y in a global scope
#whereas the local variable only works inside foo() or local scope.

def foo():
    y1 = "local"
foo()
#print(y1)

#Solve the issue
#A variable declared inside the function's body or in the local scope is known as local variable
#Normally, we declare a variable inside the function to create a local variable.
myGlobal = 5

def func1():
    myGlobal = 10
    print("Local variable function and defined:",myGlobal)

def func2():
    print(myGlobal)

func1()
func2()

#Or use the global keyword
y2 = 15

#Python treats x as a local variable and x is also not defined inside foo()
def foo():
    global y2
    y2 = y2 * 2
    print(y2)
foo()
print("Global var outside:",y2)

#Global variable and Local variable with same name
#When we print the variable inside the foo() it outputs local x: 10, this is called local scope of variable.
#Similarly, when we print the variable outside the foo(), it outputs global x: 5, this is called global scope of variable.

x = 5

def foo():
    x = 10
    print("Same name, local x:", x)

foo()
print("Same name, global x:", x)

#Non local variable (Conclusion: substitute the value of a var that you have been using in the local context)
#We use nonlocal keyword to create nonlocal variable
#Note : If we change value of nonlocal variable, the changes appears in the local variable.
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

#Others..
def globalfunc():
    print("Hello local function")
