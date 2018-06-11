#pyunit framework

import unittest
from sample_pyunit1 import fun, capital_case

class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(fun(3), 4)
    def test2(self):
        self.assertEqual(capital_case('semaphore'),'semaphore')
    def test3(self):
        self.assertEqual(fun(1), 2)
