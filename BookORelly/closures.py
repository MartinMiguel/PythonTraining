#https://www.programiz.com/python-programming/closure
#The criteria that must be met to create closure in Python are summarized in the following points.

#We must have a nested function (function inside a function).
#The nested function must refer to a value defined in the enclosing function.
#The enclosing function must return the nested function.

#Closures can avoid the use of global values and provides some form of data hiding.
#It can also provide an object oriented solution to the problem.

#When there are few methods (one method in most cases) to be implemented in a class,
#closures can provide an alternate and more elegant solutions. But when the number of
#attributes and methods get larger, better implement a class.

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

#Here is a simple example where a closure might be more preferable than defining a
# class and making objects. But the preference is all yours.
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)
# Output: 27
print(times3(9))

# Multiplier of 5
times5 = make_multiplier_of(5)
# Output: 15
print(times5(3))
# Output: 30
print(times5(times3(2)))