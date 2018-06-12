#pyunit framework

import unittest
from sample_pyunit1 import fun, capital_case


def setup_module(module):
    print("setup_module in action!!!     module:%s" % module.__name__)

def teardown_module(module):
    print("teardown_module closing!!! module:%s" % module.__name__)

class MyTest(unittest.TestCase):

    def setup_class(cls):
        print("setup_class       class:%s" % cls.__name__)

    def teardown_class(cls):
        print("teardown_class    class:%s" % cls.__name__)

    def test1(self):
        self.assertEqual(fun(3), 4)

    def test2(self):
        self.assertEqual(capital_case('semaphore'),'semaphore')

    def test3(self):
        self.assertEqual(fun(1), 2)
