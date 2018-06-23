#https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

# Assign functions to variables
def greet(name):
    return "hello "+name

greet_someone = greet
print (greet_someone("John"))

#Define functions inside other functions (Closures)
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


