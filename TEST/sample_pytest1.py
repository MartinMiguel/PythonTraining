import time

def sum(num1, num2):
    print("Sum of 2 numbers")
    print("Start : %s" % time.ctime())
    time.sleep(5)
    print("End 5 secs : %s" % time.ctime())
    return num1 + num2


def sum_only_positive(num1, num2):
    if num1 > 0 and num2 > 0:
        print("sum_only_positive function")
        print("Start : %s" % time.ctime())
        time.sleep(5)
        print("End 5 secs : %s" % time.ctime())
        return num1 + num2
    elif num1 == 15 and num2 == 14:
        x = num1
        return x + num2
    else:
        print("None function")
        print("Start : %s" % time.ctime())
        time.sleep(5)
        print("End 5 secs : %s" % time.ctime())
        return None

def mult(num1, num2):
    return num1 * num2