import unittest
from sample import sum, sum_only_positive

#class MyTest(unittest.TestCase):
#    def test_sum(self):
#      self.assertEqual(sum(5, 5),10)

#    def test_sum_positive_ok(self):
#        self.assertEqual(sum_only_positive(2, 2),4)

#    def test_sum_positive_fail(self):
#        self.assertEqual(sum_only_positive(-1, 2), None)

def test_sum():
    assert sum(5, 5) == 10

def test_sum_positive_ok():
    assert sum_only_positive(1, 2) == 4

def test_sum_positive_fail():
    assert sum_only_positive(-1, 2) is None