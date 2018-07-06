def solution(N, S, T):
    #write your code in Python 3.6
    #Print Received N,S,T
    print("Table:",N)
    print("Corner ship points:",S)
    print("Hits:",T)

    # creating table
    Table = [[0 for x in range(N)] for x in range(N)]
    print("Initializing Matrix Table:",Table)

    # slicing to separate strings from numbers
    # Change from string to int
    SRows=S[::3]
    #SRows = int(''.join(str(e) for e in S[::3]))
    #SRows = int(''.join(str(e) for e in S[::3]))
    #SRows = list(map(int, S[::3]))
    SCols=S[1::3]
    #SCols = int(''.join(str(e) for e in S[1::3]))
    print("S Rows:", SRows)
    print("S Cols:", SCols)
    TRows = T[::3]
    #TRows = int(''.join(str(e) for e in T[::3]))
    TCols = T[1::3]
    print("T Rows", TRows)
    print("T Cols", TCols)

    #Map Columns to Numbers
    ColsMap = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
             'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
             'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
             }
    SColsNum=[]
    for i in SCols:
        SColsNum.append(ColsMap[i])
    #Changing from list to string to integer
    SColsNum = ''.join(str(e) for e in SColsNum)
    print("Mapped S Colums Letters to Numbers:", SColsNum)
    TColsNum=[]
    for i in TCols:
        TColsNum.append(ColsMap[i])
    # Changing from list to string to integer
    TColsNum = ''.join(str(e) for e in TColsNum)
    print("Mapped T Colums Letters to Numbers:",TColsNum)


    #Ships filled
    x=0
    for k in range(0,int(len(SRows)/2)):
        for i in range(int(SRows[x]),int(SRows[x+1])+1):
             for j in range(int(SColsNum[x]),int(SColsNum[x+1])+1):
                 Table[i-1][j-1]=1
        x=x+2
    print("Ships filled:",Table)

    # Hits filled
    for i in range(int(len(TRows))):
        Table[int(TRows[i])-1][int(TColsNum[i])-1] = 2
        #print(i)
        #print("Hits filled:", Table)
    #Table[1][2] = 2
    print("Hits filled:", Table)
    pass

N = 4
S = "1B 2C 2D 4D"
T = "2B 2D 3D 4D 4A"
solution(N,S,T)