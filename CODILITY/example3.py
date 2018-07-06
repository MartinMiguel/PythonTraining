def solution(N, S, T):
    # write your code in Python 3.6
    print(N)
    print(S)
    print(T)

    A = [0] * N
    for i in range(N):
        A[i] = [0] * N
    print(A)
    SN=S[::3]
    SL=S[1::3]
    print("Slicing: S", S[::3])
    print("Slicing: S", SL)
    TN = T[::3]
    TL = T[1::3]
    print("Slicing: T", T[::3])
    print("Slicing: T", TL)

    dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
             'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
             'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
             }
    NewSL=[]
    for i in SL:
       # print(i)
        NewSL.append(dict[i])
    print(NewSL)
    NewTL=[]
    for i in TL:
       # print(i)
        NewTL.append(dict[i])
    print(NewTL)

    #Fill ships
    for i in SN[::2]:
        #print(i)
        #for i in range(A):
           #for j in range(A):
               #print(i,j)

        for j in NewSL[::2]:
            print(i,j)
        #for i in range(A):
           #for j in range(A):
               #print(i,j)



            #Y=list(dict.values())
    #if 1 in Y:
        #print("Yes")
        # print("Yes")
    #print(Y)
    #a = []
    #for i in S:
        #print("Hey:",i)
        #print(S)
        #print(dict.values())
        #if i in Y:
            #a.append(i)
            #print("Yes",i)
            #break
    #print(a)
        #a.append(i)
   # a  # the list with the new items.

    pass

N = 4
S = "1B 2C 2D 4D"
T = "2B 2D 3D 4D 4A"
solution(N,S,T)