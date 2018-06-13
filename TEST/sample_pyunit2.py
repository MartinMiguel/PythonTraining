import time
def multiply(a, b):
    print("Waiting 3 secs")
    time.sleep(3)
    print ("a and b values are: %i and %i", a, b)
    time.sleep(2)
    return a * b

def multiply2(a, b):
    print("Waiting 3 secs for 2 mult")
    time.sleep(3)
    print ("a and b values *2 are: %i and %i", a, b)
    time.sleep(2)
    return a * b * 2