def identity(n):
    m=[[0 for x in range(n)] for y in range(n)]
    for i in range(0,2):
        print("i,n",i,n)
        m[i][i] = 1
    print(m)

identity(3)

for x in range(2, 6):
  print(x)