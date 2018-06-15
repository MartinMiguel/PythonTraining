#https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

# Assign functions to variables
def greet(name):
    return "hello "+name

greet_someone = greet
print (greet_someone("John"))

#Define functions inside other functions
def greet(name):
    def get_message():
        return "Hello "

    result = get_message()+name
    return result

def f(x):
    def g(y):
        return y + x + 3
    return g

nf1 = f(1)
nf2 = f(3)

print(nf1(1))
print(nf2(1))

print (greet("John"))

#Functions can be passed as parameters to other functions
def greet(name):
   return "Hello " + name

def call_func(func):
    other_name = "John"
    return func(other_name)

print (call_func(greet))

#Functions generating other functions.
def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message

greet = compose_greet_func()
print (greet())

#Decorator Functions
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

my_get_text = p_decorate(get_text)
print (my_get_text("John"))

#Python's Decorator Syntax, we don't have to get_text = p_decorator(get_text)
def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

@p_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print (get_text("John"))

#Best Example for decorators without args and kwargs
import time

def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        print("First time:",t1)
        some_function()
        t2 = time.time()
        print("Second time:",t2)
        return "Time it took to run the function: " + str((t2 - t1))
    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("Sum of all the numbers: " + str(sum(num_list)))


print(my_function())

#Decorating Methods *args
def p_decorate(func):
   def func_wrapper(*args):
       print("Start Decoration")
       return "<p>{0}</p>".format(func(*args))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"
        self.middle = "Poodle"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family+" "+self.middle

my_person = Person()
print(my_person.get_fullname())

