
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

#Python has overloading special functions as _add_  Internally: p1.__add__(p2)
#https://www.programiz.com/python-programming/operator-overloading

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(2, 3)
p2 = Point(-1, 2)
print(p1 + p2)