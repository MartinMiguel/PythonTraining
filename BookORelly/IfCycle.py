a = [1, 2, 3, 4, 5]
b = [2, 3]
if b in a:
    print("True: ", *a)
else:
    print("False: ", *a)
a = str(a)[1:-1]
print("String conversion: ", a)
print("\n")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

t = 1
d = 1
if t == 2:
    d = 2
    print(t)
print(d)
