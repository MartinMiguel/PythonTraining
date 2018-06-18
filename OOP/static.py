#Class or static variables in python
#Variables declared inside the class definition, but not inside a method are class or static variables:
#Conclusion: Create a new instance of a class variable (Example 1 and 2)and modify it or change the
#class variable value (Example 3)

#Example 1
class MyClass:
    i = 3
print("My class variable, It will Print 3: ",MyClass.i)
#Instantiation
m = MyClass()
#Set the value of my variable instantiated
m.i = 4
print("My class variable is 3: ",MyClass.i, "My instantiated variable is 4: ",m.i)
#########################################################################################
#Example 2
#Instance a class variable
class CSStudent:
    stream = 'cse'  # Class Variable
    def __init__(self, name, roll):
        self.name = name  # Instance Variable
        self.roll = roll  # Instance Variable

a = CSStudent('Geek', 1)   #Instantiate for name and roll
b = CSStudent('Nerd', 2)

print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.name)    # prints "Geek"
print(b.name)    # prints "Nerd"
print(a.roll)    # prints "1"
print(b.roll)    # prints "2"
# Class variables can be accessed using class name also
print(CSStudent.stream)  # prints "cse"
#########################################################################################
#Example 3
#Instance that variable from a class and start playing with it (modifying).
#You can keep modifying an instanced class variable or
#Set the class variable to a new value

class Example:
    staticVariable = 5 # Access through class

print("Prints 5: ",Example.staticVariable)
#Instance
instance = Example()
print("Prints 5: ", instance.staticVariable) #
instance.staticVariable = 6
print("Prints 6: ", instance.staticVariable)
print("Prints 5: ", Example.staticVariable) # 5
#We should change class variables using class name only.
Example.staticVariable = 7
print ("Prints 6: ", instance.staticVariable) # still 6
print ("Prints 7: ", Example.staticVariable) # now 7
#########################################################################################