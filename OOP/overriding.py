#Overriding a method. Inherit the methods and parameters from a base class, use the methods needed
#and override or write new methods with different name as needed

class Base(): # Base class

    '''def add(self,a,b):
        s=a+b
        print s'''

    test_var = 5

    def add(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

        sum =a+b+c
        print("Superclass sum of a,b and c:", sum)

class Derived(Base): # Derived class

    def add(self,a,b): # overriding method
        sum=a+b
        print("Subclass sum of a and b:",sum)

add_fun_1=Base()     #instance creation for Base class
add_fun_2=Derived()  #instance creation for Derived class

add_fun_1.add(4,2,5) # function with 3 arguments
add_fun_2.add(4,2)   # function with 2 arguments