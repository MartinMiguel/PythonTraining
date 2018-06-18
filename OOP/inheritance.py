class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      self.a = 1
      print ("Calling parent constructor, a value:", self.a)

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

   def myMethod(self):
      print('Calling parent method')

class Child(Parent):    #define child class
   def __init__(self):  #overriding
      self.a = 2
      print ("Calling child constructor, a value:", self.a)

   def childMethod(self):
      print ('Calling child method')
       
   #Overriding Method (same name of method as parent)
   def myMethod(self):
      print('Calling my child method')


c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.getAttr()          # again call parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
c.myMethod()         # child calls overridden method