#Several ways to call a method (method overloading)
#Depending on the function definition, it can be called with zero, one, two or more parameters.

class Human:

    def sayHello(self, name=None):

        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')

# Create instance
obj = Human()

# Call the method
obj.sayHello()

# Call the method with a parameter
obj.sayHello('Guido')