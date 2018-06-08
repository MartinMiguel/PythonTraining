#Sets:
#-Unordered with no duplicate elements
#-Declared with curly braces or set keyword
#-Since can't be look by index you can't modify a set element
#-Contents are mutable through operations as add, pop, remove.
#-Can't support operations with lists, only tuples
#-Used for mathematical operations

#Tuples:
#-Can have duplicate elements
#-Declared using parentheses or tuple keyword
#-Inmuttable, can't change elements and contents
#-Can look by index and slicing
#-tuples can contain mutable objects as lists
#Difference with set is that not even object change is allowed with tuples (update tuples, only taking portions of
#existing tuples to create new tuples)
#*********************************************
#The set type is mutable -- the contents can be changed using methods like add() and remove().
#Since it is mutable, cannot be used as either a dictionary key or as an element of another set.

#The frozenset type is immutable and its contents cannot be altered after is created; however,
#it can be used as a dictionary key or as an element of another set.

#Conclusion: user can remove and add elements (object set is mutable), but you can't change an element
#since elements are immutable so indexing is not supported, e.g.
#A = {2, 3, 5, 4}
#A[0] = 1
#Difference is that you can change the set object with methods as add, remove pop

#Can't support operations with lists, only tuples
#Since Sets do not record element position or order of insertion, can't be looked by index.
#unordered collection with no duplicate elements
#faster than list and tuples
#create a set by using function set or using curly braces {}, set classes are implemented using dictionaries.

#sets can be used to filter duplicates out of other collections
#sets can be used to perform mathematical operations as union, intersection ...

#Inmmutable or Frozen set
#ImmutableSet objects do not have methods for adding or removing elements.
#union, copy, x in s, len(s)
#3.-Intersection
A = {2, 3, 5, 4}
B = {2, 5, 100}
print("B intersection A:",B.intersection(A))

#the following table lists operations available in Set but not found in ImmutableSet:
#add,remove,pop,discard

#Add tuple to a set
vowels = {'a', 'a', 'e', 'i', 'i'}
tup = ('o','u')
vowels.add(tup)
print('Vowels are:', vowels)
print("set with tuple:",type(vowels))

#Error unhashable list operation with sets
vowels1 = {'ac', 'ac', 'ec', 'ic', 'ic'}
list1 = ['o','u']
#vowels1.add(list1)
#print("Vowels set with list embedded:",vowels1)

#methods
#1.-Remove
language = {'English', 'French', 'German'}
language.remove('German')
print('Updated language set: ', language)

#2.-Add
vowels = {'a', 'e', 'i', 'u'}
vowels.add('oz')
print('Vowels are:', vowels)

#4.-Sort descendent
pySet = {'e', 'a', 'u', 'o', 'i'}
print(sorted(pySet, reverse=True))

#Others..
A= {1, 2, 3, 4}
print(A)
S = set() # Initialize an empty set
S.add(1.23)
S.add((1, 2, 3))
print(S)
