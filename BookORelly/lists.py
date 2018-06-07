#definition with square bracket
#can be modified and updated
#can have numbers with chars
#support indexing
#metodos: del, + for concatenation, repetition *, append
#when to use lists: similar tu using arrays in C
#list are used when something is going to change

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

#Accessing values through slicing
print("Slicing:", list1[0:2:1])
list1[0] = "mathematician"
print("Substitution through slicing:", list1[:])

#modify numbers
list1[2]=list1[2]-1
print("Numbers operation:", list1[0:4])

#adding numbers
list1[-1:-2] = "N"
print("Slicing modified:", list1[:-1],list1[-1])

#searching
L = [1, 2, 1, 3, 2, 4, 5]
print(set(L))
engineers = {'bob', 'sue', 'ann', 'vic'}
print( 'bob' in engineers )

#methods
del list1[-2]
print("\nMethods, deletion:", list1[0:])
print("Length:", len(list2))
list4=list1+list2
print("Concatenation:", list4)
list1 = list1*2
print("Repetition:", list1)
del list1[0:3]
print("Delete",list1)
list2.insert(3,3.5)
print("Insert new Element",list2)
print("Max:",max(list2))
list2.reverse()
print("Reverse:",list2)

#lists as stacks, use collections.deque which was designed to have fast appends and pops from both ends.
list2.append(6)
print("\nAppend, Stack: ",list2)
list2.pop()
print("Append, Stack: ",list2)

#Powerful functions
#1.-filter()
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(alphabet in vowels):
        print("alphated,vowels", alphabet, vowels)
        return True
    else:
        return False
filteredVowels = filter(filterVowels, alphabets)
print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)

#Extra
S= 'shrubbery'
L = list(S) # Expand to a list: [...]
print(L)
print(type(L))

L = [123, 'spam', 1.23]
print(len(L))
print(L[:-1])
print(L.pop(2))
print(L)
M = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
