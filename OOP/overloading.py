#Overloading with function decorators, Ideal when you need to extend the
#functionality of functions that you don't want to modify
#Best to use args o kwargs when you don't know how many arguments are you
#going to pass

#Example 1
class Human:
    def sayHello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')

obj = Human()           #create a instance
obj.sayHello()          #call instance method
obj.sayHello('Guido')

#Example 1.2
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)

##################################################
#Example 2
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
##################################################
#Example 3
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

print_everything('s1', 's2', 's3')
print_everything('s4', 's5')

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')

#Example 4

class args_example:

    def print_everything1(*args):
      for count, thing in enumerate(args):
          print('{0}. {1}'.format(count, thing))

    print_everything1('apple', 'banana', 'cabbage')
    print_everything1('apple-orange', 'banana')

    def test_var_args2(f_arg, *argv):
        for arg in argv:
           print("another arg through *argv:", arg)

Ex1 = args_example()
Ex1.test_var_args2('nice1', 'nice2', 'nice3', 'nice4')
##################################################
#Example 5
#**kwargs allows you to pass keyworded variable length of arguments to a function.
#You should use **kwargs if you want to handle named arguments in a function.
#**kwargs = dictionary - whose keys become separate keyword arguments and the values
#become values of these arguments.
#Similarly, **kwargs allows you to handle named arguments that you have not defined in advance:

class kwargs_example:
    def table_things(**kwargs):
        for name, value in kwargs.items():
           print( '{0} = {1}'.format(name, value))

kwargs_example.table_things(apple = 'fruit', cabbage = 'vegetable')
kwargs_example.table_things(orange = 'fruit')
##################################################
#Example 6
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
##################################################
#Example 7
#You can also use the * and ** syntax when calling a function. For example:
def print_three_things(a, b, c):
    print( 'a = {0}, b = {1}, c = {2}'.format(a,b,c))

mylist = ['aardvark', 'baboon', 'cat']
print_three_things(*mylist)
##################################################
#Example 8
#Combination of args and kwargs
def total(a=5, *numbers, **phonebook):
    print('a', a)

    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    #iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))