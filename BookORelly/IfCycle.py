a = [1,2,3,4,5]
b = [2,3]
if b in a:
    print("True: ",*a)
else:
    print("False: ",*a)
a = str(a)[1:-1]
print("String conversion: ", a)