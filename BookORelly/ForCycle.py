#Range retorna una lista
a = range(5)
for x in range(len(a)):
    if a[x] == 2:
        continue
    print(a[x])

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
print("Append items on empty list: ",squared)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "cherry":
    break
  print(x)

for x in range(2, 4):
    print(x)