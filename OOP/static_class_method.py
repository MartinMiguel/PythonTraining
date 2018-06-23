#Class and static methods are decorators
#classmethod must have a reference to a class object as the first parameter
#staticmethod can have no parameters at all.

#1.-classmethod decorator
class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {} new robot and added to population)".format(self.name))    #format to print inside {}

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    # equivalent to Robot.population
    def how_many(cls):
        """Prints the current population."""
        #cls.population equivalent to Robot.population
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()

##################################################################
#https://www.geeksforgeeks.org/class-method-vs-static-method-python/
#https://www.programiz.com/python-programming/methods/built-in/staticmethod

#A class method takes cls as first parameter while a static method needs no specific parameters.
#A class method can access or modify class state while a static method can’t access or modify it.
#In general, static methods know nothing about class state. They are utility type methods that
#take some parameters and work upon those parameters. On the other hand class methods must have
#class as parameter.

#We generally use class method to create factory methods. Factory methods return class object
#( similar to a constructor ) for different use cases.

#Static methods have very limited use case, because like class methods or any other methods
#within a class, they cannot access properties of the class itself.

#However, when you need a utility function that doesn't access any properties of a class but
#makes sense that it belongs to the class, we use static functions.

#Conclusion: Usar static method cuando quieres tener una utileria relacionada a la clase pero
#que esta aislada y no accesa ningura propiedad de la clase
#Usar

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name_b, birthYear):
        #equivalent to Person(name, 2008 - birthYear)
        #return Person(name_b, 2018-birthYear)
        return cls(name_b, 2018 - birthYear)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(ageX):
        return ageX > 18

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
person1.display()
person.display()

print(Person.isAdult(22))
##########################################
class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

if (date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")
##############################################
#3.-Acceso de class method a las variables
class Pizza(object):

    wrad = 10

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    @staticmethod
    def compute_area(radius):
         return 1 * (radius * 2)

    @classmethod
    def compute_volume(cls, heightX, radiusX):
         return heightX * cls.compute_area(radiusX)

    @classmethod
    def super_compute(cls,aument):
        radius_i= cls.wrad * aument
        height_i=14
        return radius_i*height_i

    def get_volume(self):
        return self.compute_volume(self.height, self.radius)


m=Pizza(1,2)
print(m.compute_area(5)) #8 separate method
print(m.compute_volume(2,3))
print("Get vol:",m.get_volume())
m.super_compute(10)
print(Pizza.height)
#m.display()