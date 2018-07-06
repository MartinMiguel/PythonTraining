def solution(A):
    # write your code in Python 3.6

    missing = 1
    for elem in sorted(A):
        if elem == missing:
            print("N")
            missing += 1
        if elem > missing:
            print("Y")
            break
        print("elemen:",elem)
        print("missing:",missing)
        print("\n")
    return missing
    pass


D = [-1,-3,1,2,1,0,10,3,4,6,5,1000]
print("Solution:",solution(D))