# lambda is used to create what is known as anonymous functions. These are essentially functions with no pre-defined
# name. They are good for constructing adaptable functions, and thus good for event handling.
# can replace lambda by function
# Python's lambda keyword: unnecessary, occasionally useful.

myfunc = lambda i: i*2
print("Pass arg:",myfunc(2))

myfunc = lambda x,y: x*y
print(myfunc(3,6))

def myfunc(n):
  return lambda i: i*n

doubler = myfunc(2)
tripler = myfunc(3)
val = 11
print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)))

mult3 = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(*mult3)

def transform(n):
    return lambda x: x + n
f = transform(3)
print("Hold param:",f(4))

#A return statement with no arguments is the same as return None.
def printme( str ):
   print (str)
   return
printme("I'm first call to user defined function!")

#All parameters (arguments) in the Python language are passed by reference. It means if you change
#what a parameter refers to within a function, the change also reflects back in the calling function.
def changeme(mylist2):
   mylist2.append([1,2,3,4])
   print ("Values inside the function: ", mylist2)
   #local to the function
   mylist = [1, 2, 3, 4]
   print("Local values inside the function: ", mylist)
   return

mylist = [10,20,30]
changeme(mylist)
print ("Values outside the function: ", mylist)

# Default values if not initialized
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age ", age)
   return

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )