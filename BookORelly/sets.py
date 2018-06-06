#Sets are also mutable so their contents can change. The difference with tuples is that can't be changed and can
#be looked by index
#it's faster than list and tuples

# sets because items are stored only once in a set, sets can be used to filter duplicates out of other collections
# can convert to sets and play with math and logical operations.

#unordered collection with no duplicate elements
#sets can be used to perform mathematical operations as union, intersection ...
#create a set by using function set or using curly braces {}
#can't be looked by index
#objects of different types

#Sets dont support indexing
#print('Vowels[0]:',vowels[0])

#Add tuple to a set
vowels = {'a', 'a', 'e', 'i', 'i'}
tup = ('o','u')
vowels.add(tup)
print('Vowels are:', vowels)
print("set with tuple:",type(vowels))

#methos
#1.-Remove
language = {'English', 'French', 'German'}
language.remove('German')
print('Updated language set: ', language)

#2.-Add
vowels = {'a', 'e', 'i', 'u'}
vowels.add('o')
print('Vowels are:', vowels)

#3.-Intersection
A = {2, 3, 5, 4}
B = {2, 5, 100}
print("B intersection A:",B.intersection(A))

#4.-Sort descendent
pySet = {'e', 'a', 'u', 'o', 'i'}
print(sorted(pySet, reverse=True))

#Others..
A= set([1, 2, 3, 4])
print(A)
S = set() # Initialize an empty set
S.add(1.23)
S.add((1, 2, 3))
print(S)
L = [1, 2, 1, 3, 2, 4, 5]
print(set(L))
engineers = {'bob', 'sue', 'ann', 'vic'}
print( 'bob' in engineers )