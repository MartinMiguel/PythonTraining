#https://www.blog.pythonlibrary.org/2016/06/10/python-201-what-are-descriptors/
#http://python-textbok.readthedocs.io/en/1.0/Classes.html
#__get__(self, obj, type=None), returns value
#__set__(self, obj, value), returns None
#__delete__(self, obj), returns None

#You can also use a different method to update the value of the attribute instead of accessing it
#directly. Methods like this are called getters and setters, because they “get” and “set” the values
#of attributes, respectively.

#In some languages you are encouraged to use getters and setters for all attributes, and never to
#access their values directly – and there are language features which can make attributes inaccessible
#except through setters and getters.

#In Python, accessing simple attributes directly is perfectly acceptable, and writing getters and setters
#for all of them is considered unnecessarily verbose. Setters can be inconvenient because they don’t allow
#use of compound assignment operators:

#__init__ es el constructor de tu clase en el creas una nueva instancia de la clase
#Python has the destructor concept - the __del__ method

#Ejemplo 1
class perro():

  def __init__(self, nombre, size, raza):
      self.nombre=nombre
      self.size=size
      self.raza=raza

  def ladra(self):
     s=""
     for l in self.nombre:
      s+="wof"
     print(s)

chucho=perro("Chucho","grande","husky")
print(chucho.nombre)
chucho.ladra()

cloe=perro("cloe","mini","chihuahua")
cloe.ladra()

######################################################
#Ejemplo 2
class Clazz():
    def getName(self):
        return self.__class__.__name__

c=Clazz()
print("Class Name:",c.getName())

######################################################
#Ejemplo 3
class Point:
   #Constructor
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   #Destructor
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print (id(pt1), id(pt2), id(pt3)) # prints the ids of the objects
del pt1
del pt2
del pt3
#print (id(pt1), id(pt2), id(pt3)) # error objects deleted

#########################################################################

#Example 4
class MyDescriptor():
    """
    A simple demo descriptor
    """

    def __init__(self, initial_value=None, name='my_var'):
        self.var_name = name
        self.value = initial_value

    def __get__(self, obj, objtype):
        print('Getting', self.var_name)
        return self.value

    def __set__(self, obj, value):
        msg = 'Setting {name} to {value}'
        print(msg.format(name=self.var_name, value=value))
        print("Hit...")
        self.value = value

class MyClass():
    desc = MyDescriptor(initial_value='Mike', name='descp')
    normal = 10

if __name__ == '__main__':
    c = MyClass()
    print(c.desc)
    print(c.normal)
    c.desc = 100
    print(c.desc)

#########################################################################

# Example 5
class Person:
    def __init__(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height


jane = Person(153) # Jane is 153cm tall
print("jane is:",jane.height)
jane.height += 1                 # Jane grows by a centimetre
jane.set_height(jane.height + 1) # Jane grows again
print("jane is:",jane.height)
print("jane is:",jane.get_height())

#As we can see, incrementing the height attribute through a setter is much more verbose.