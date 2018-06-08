#Class or static variables in python
#Variables declared inside the class definition, but not inside a method are class or static variables:

class MyClass:
    #class-level i variable
    i = 3

print(MyClass.i)
m = MyClass()
m.i = 4
#This is different from C++ and Java, but not so different from C#, where a static member can't be accessed
#using a reference to an instance.
print(MyClass.i, m.i)

#Instance a class variable
class CSStudent:
    stream = 'cse'  # Class Variable
    def __init__(self, name, roll):
        self.name = name  # Instance Variable
        self.roll = roll  # Instance Variable

a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.name)  # prints "Geek"
print(b.name)  # prints "Nerd"
print(a.roll)  # prints "1"
print(b.roll)  # prints "2"

# Class variables can be accessed using class name also
print(CSStudent.stream)  # prints "cse"

#Instance that variable from a class and start playing with it (modifying).
#You can keep modifying an instanced class variable or
#Set the class variable to a new value

class Example:
    staticVariable = 5 # Access through class

print(Example.staticVariable) # prints 5
# Access through an instance
instance = Example()
print(instance.staticVariable) # still 5
# Change within an instance
instance.staticVariable = 6
print(instance.staticVariable) # 6
print(Example.staticVariable) # 5

# Change through
#We should change class variables using class name only.
Example.staticVariable = 7
print (instance.staticVariable) # still 6
print (Example.staticVariable) # now 7