#clase define un tipo de objeto, cuando lo llamas estas creando una instancia de esa clase,
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