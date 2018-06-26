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

###########################################
#Decorating Methods with overloading(*args)
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
###########################################
#Decorating Methods with overloading(*args) and (**kwargs)
def method_decorator(fn):
    "Example of a method decorator"
    def decorator(*args, **kwargs):
        print ("\tInside the decorator")
        return fn(*args, **kwargs)

    return decorator

class MyFirstClass(object):
    """
    This class has all its methods decorated
    """
    @method_decorator
    def first_method(self, *args, **kwargs):
        print ("\t\tthis is a the MyFirstClass.first_method")

    @method_decorator
    def second_method(self, *args, **kwargs):
        print ("\t\tthis is the MyFirstClass.second_method")

if __name__ == "__main__":
    print ("::: With decorated methods :::")
    x = MyFirstClass()
    x.first_method()
    x.second_method()
