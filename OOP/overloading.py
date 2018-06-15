#Overloading with function decorators, Ideal when you need to extend the
#functionality of functions that you don't want to modify

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

#Overloading in a python way
#https://stackoverflow.com/questions/3394835/args-and-kwargs

#Writing *args and **kwargs is just a convention.
#*args is used to send a non-keyworded variable length argument list to the function.
#*args = list of arguments - as positional arguments
#You would use *args when you're not sure how many arguments might be passed to your function,
#i.e. it allows you pass an arbitrary number of arguments to your function. For example:

def print_everything(*args):
    for count, thing in enumerate(args):
        print('{0}. {1}'.format(count, thing))

print_everything('apple', 'banana', 'cabbage')
print_everything('apple-orange', 'banana')

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')

#**kwargs allows you to pass keyworded variable length of arguments to a function.
#You should use **kwargs if you want to handle named arguments in a function.
#**kwargs = dictionary - whose keys become separate keyword arguments and the values
#become values of these arguments.
#Similarly, **kwargs allows you to handle named arguments that you have not defined in advance:

def table_things(**kwargs):
    for name, value in kwargs.items():
        print( '{0} = {1}'.format(name, value))

table_things(apple = 'fruit', cabbage = 'vegetable')
table_things(orange = 'fruit')

#You can use these along with named arguments too. The explicit arguments get values first
#and then everything else is passed to *args and **kwargs. The named arguments come first
#in the list. For example:
def add(instanceOf, *args):
    if instanceOf == 'int':
        result = 0
    if instanceOf == 'str':
        result = ''
    if instanceOf == 'doub':
        result = 'My '
    for i in args:
        result = result + i
    return result

print(add('int', 3, 4, 5))
print(add('str', 'I', ' am', ' in', ' Python'))
print(add('doub','kiss'))

#You can also use the * and ** syntax when calling a function. For example:
def print_three_things(a, b, c):
    print( 'a = {0}, b = {1}, c = {2}'.format(a,b,c))

mylist = ['aardvark', 'baboon', 'cat']
print_three_things(*mylist)