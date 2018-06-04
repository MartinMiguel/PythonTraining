import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(fun(3), 4)
    def test2(self):
        self.assertEqual(capital_case('semaphore'),'semaphore')

def capital_case(x):
    return x.capitalize()
