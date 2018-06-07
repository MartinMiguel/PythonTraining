
#Instance − An individual object of a certain class. An object obj that belongs to a class Circle,
# for example, is an instance of the class Circle.

class Employee:
    'Common base class for all employees'
    #variable empCount is a class variable whose value is shared among all instances of a this class.
    empCount = 0
    #class constructor or initialization method that Python calls when you create a new instance of this class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)
emp1.age = 7  # Add an 'age' attribute.
print("Employee 1 age:", emp1.age)
del emp1.age  # Delete 'age' attribute.
print("Attribute age exists for emp1?: ", hasattr(emp1, 'age'))    # Returns true if 'age' attribute exists
emp1.age = 8  # Modify 'age' attribute.
print("Value of age attribute por emp1: ", getattr(emp1, 'age'))    # Returns value of 'age' attribute

#Class attributes
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)