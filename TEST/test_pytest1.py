#Pytest
#http://pythontesting.net/framework/pytest/pytest-introduction/
#There is no need to import unittest
#There is no need to derive from TestCase
#There is no need to for special self.assertEqual()

import unittest
from sample import sum, sum_only_positive

#class MyTest(unittest.TestCase):

def test_sum():
    assert sum(5, 5) == 10

def test_sum_positive_ok():
    assert sum_only_positive(1, 2) == 4

def test_sum_positive_fail():
    assert sum_only_positive(-1, 2) is None