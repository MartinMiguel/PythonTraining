# clase define un tipo de objeto, cuando lo llamas estas creando una instancia de esa clase,
#__init__ es el constructor de tu clase en el creas una nueva instancia de la clase

#1.-Ejemplo 1
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

#wofwofwofwofwofwof
cloe=perro("cloe","mini","chihuahua")
cloe.ladra()

#wofwofwofwof

