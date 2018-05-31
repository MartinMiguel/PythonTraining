#extended slice
S = 'abcdefghijklmnop'
print(S[::2])
print(S[1:10:2])
num = 1 / 3.0
print(num)
print('%4.2f' %num)
# sets because items are stored only once in a set, sets can be used to filter duplicates out of other collections
# can convert to sets and play with math and logical operations. Works for large databases
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
# These links from variables to objects are called references in Python—that is, a reference is a kind of association, implemented as a pointer in memory
# This automatic reclamation of objects’ space is known as garbage collection,
# copies
L1 = [2, 3, 4]
L2 = L1[:] # Make a copy of L1 (or list(L1), copy.copy(L1), etc.)
L1[0] = 24
print(L2)
#Single- and Double-Quoted Strings Are the Same
#Indexing and Slicing
#Extended slicing
S = 'abcdefghijklmnop'
print(S[1:10:2])
S = 'hello'
print(S[::-1])
S = 'splot'
print(S.replace('pl', 'pamal'))
print('That is %d %s bird!' % (1, 'dead'))
S = 'spam'
print(S.find('pa'))
S = 'spammy'
#String methods
print(S[:3] + 'xx' + S[5:])
print(S.replace('mm', 'xx'))
#string formats
template = '{motto}, {pork} and {food}' # By keyword
L= template.format(motto='spam', pork='ham', food='eggs')
print(L)
print("Chapter5")