#http://python-textbok.readthedocs.io/en/1.0/Classes.html
#Hard to see difference between classmethod and setter
#The @property decorator can be used to implement a getter for your class' instance variable, however you can
#use also classmethod for this

#The @property decorator lets us make a method behave like an attribute

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return "%s %s" % (self.name, self.surname)

    @classmethod       # similar to a get but can modify the class variables assign them with modification
    def fullname2(cls,name1,surname):
        name2 = name1 + "Nes"
        return cls(name2, surname)

    def display(self):
        print(self.name + " " + self.surname)

jane = Person("JaneX", "SmithX")
print(jane.fullname) # no brackets!
name1=Person.fullname2("John","Connor")
print(name1.display())

##############################################

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

#The @property decorator can be used to implement a getter for your class' instance variable
    @property
    def fullname(self):
        return "%s %s" % (self.name, self.surname)  + " Yes"

   # @fullname.setter
   # def fullname(self, value):
    #    this is much more complicated in real life
    #    name, surname = value.split(" ", 2)
    #    self.name = name
    #    self.surname = surname

    @fullname.deleter
    def fullname(self):
        del self.name
        del self.surname

jane = Person("Jane", "Smith")
print(jane.fullname)

#jane.fullname = "Jane Doe" #This is a setter, for this it is used @fullname.setter like classmethod
print(jane.fullname)
print(jane.name)
print(jane.surname)