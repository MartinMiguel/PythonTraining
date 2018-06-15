#Tuples use parenthesis can be declared using tuple

#Cant change elemets
#tup1 = (12, 34.56);
#tup1[0] = 100;
#Difference with set is that not even object change is allowed with tuples (update tuples, only taking portions of
#existing tuples to create new tuples)

#add, remove, pop methods not supported
#tuples can be sliced, concatenated, ... as operations
#tuples can contain mutable objects as lists
#when tu use tuples: similar tu using structs in C
#What you are likely to do with a tuple is access the elements individually and do specific
#things with them. Use a tuple when the positions themselves are the best identifiers you can use for the data

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
#empty tuple
tup4 = ()
#To write a tuple containing a single value you have to include a comma, even though there is only one value
tup5 = (3,)

#Accessing values through slicing
print("Slicing:", tup1[0:2:1])
#tup1[0] = "mathematician" error tuples don't support item assignment

#To update tuples, only taking portions of existing tuples to create new tuples
tup6 = tup1[:] +tup2
print("tup6: =tup1+tup2 ",tup6)

#Tuple delete
del tup6
#print("tup 6 del: " tup6) error tuple deted

#Convert a list in tuple
list1 = [1,4,3]
tup7 = tuple(list1)
print("tupe7:", tup7)
print("compare 2 tuples: ",len(tup2))

#nested tuples
t = 12345, 54321, 'hello!'
u = t, tup7
print("u nested: ",u)
print("u len:", len(u))
print("u[0]:", u[0])

#tuples containing mutable objects list
list1_1 = [10,11]
list2_1 = [12,13]
tupwlist = (list1_1, list2_1)
print("Tuple containing lists: ",list1_1, list2_1)
print("Type:",type(tupwlist))
print("tuple with lists contained:",tupwlist)
print("tuple with lists contained tupwlist[0]:",tupwlist[0])
#list1_1 is updated but still don't change due to previous assignation
list1_1 = [20,21]
#Redefinition of tupwlist to change, otherwise can't chance
tupwlist = (list1_1, list2_1, list1)
print("tuple with lists contained and updated:",tupwlist)
del(list1_1)
print("tuple with lists contained and updated with list del, not affecting:",tupwlist)
tupwlist = (list2_1, list1)
print("tuple with lists contained and updated with list redefinition, not affecting:",tupwlist)
print("Type:",type(tupwlist))
#tupwlist = (list1_1,list2_1)
print("tuple with lists contained:",tupwlist)
print("Type:",type(tupwlist))