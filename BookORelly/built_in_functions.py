#https://medium.com/@happymishra66/lambda-map-and-filter-in-python-4935f248593
#Filter (used with lists)
#unction_object is called for each element of the iterable and filter returns only those element
#for which the function_object returns true.
#Like map function, filter function also returns a list of element.
#Unlike map function filter function can only have one iterable as input.
A=list(filter((lambda x: x > 0), range(-5, 5)))
print(A)
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

#map
#map functions expects a function object and any number of iterables like list,
#dictionary, etc. It executes the function_object for each element in the sequence
#and returns a list of the elements modified by the function object.
M = map(abs, (-1, 0, 1))
print("With tuple:",next(M),next(M))
B=list(map(abs, [-1, -2, 0, 1, 2]))
print("With list:",B)
M1= map(lambda x: 1 * x, range(4))
print("2 range mult:",list(M1))

def multiply2(x):
    return x * 2

print("Multiply a list with def:",list(map(multiply2, [1, 2, 3, 4])))
print("Multiply a lambda:",list(map(lambda x : x*2, [1, 2, 3, 4])))

dict_a = {'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}
print("Output: ['python', 'java']:",list(map(lambda x: x['name'], dict_a)))
print("Output: [100, 80]:",list(map(lambda x: x['points'] * 10, dict_a)))

list_a = [1, 2, 3]
list_b = [10, 20, 30]
print(list(map(lambda x, y: x + y, list_a, list_b)))# Output: [11, 22, 33]

#difference
print("Dictionary to show diff:", dict_a)
B=list(filter(lambda x : x['name'] == 'python', dict_a)) # Output: [{'name': 'python', 'points': 10}]
print("Filter elements with the function is true:",B)
C=list(map(lambda x: x['name'] == "python", dict_a))
print("With Map returns a list of the elements modified by the function:",C)