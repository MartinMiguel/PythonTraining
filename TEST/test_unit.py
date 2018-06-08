import unittest

def fun(x):
    Y=8
    print("Y output:",Y)
    return x + 1

def capital_case(x):
    Z=8
    print("Z output:", Z)
    return x.capitalize()



class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(fun(3), 4)
    def test2(self):
        self.assertEqual(capital_case('semaphore'),'semaphore')
    def test3(self):
        self.assertEqual(fun(1), 2)
