#Class Decorating Methods with overloading(*args)
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
################################################################

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