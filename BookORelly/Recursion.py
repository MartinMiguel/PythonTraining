def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 1
    print ("end")
  return result

print("\n\nRecursion Example Results")
tri_recursion(3)

def maximum(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0],maximum(L[1:]))

L = [2, 4, 6, 23, 1, 46, 44, 102, 12]
print (maximum(L))

