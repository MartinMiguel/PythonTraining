
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  # __init__, a typical initializer of Python class instances, which receives arguments as a typical instancemethod
  #having the first non-optional argument (self) that holds reference to a newly created instance.
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

p1.age = 40
