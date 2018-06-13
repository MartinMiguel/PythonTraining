#Pytest
#http://pythontesting.net/framework/pytest/pytest-introduction/
#There is no need to import unittest
#There is no need to derive from TestCase
#There is no need to for special self.assertEqual()
#run as py.test -s module_name.py

import unittest
import time
from sample_pytest1 import sum, sum_only_positive

#class MyTest(unittest.TestCase):

def setup_module(module):
    print("setup_module in action!!!     module:%s" % module.__name__)
    print("Setup")
    print("Start : %s" % time.ctime())
    time.sleep(15)
    print("End 2 secs : %s" % time.ctime())

def teardown_module(module):
    print("teardown_module closing!!! module:%s" % module.__name__)
    print("Tear down")
    print("Start : %s" % time.ctime())
    time.sleep(15)
    print("End 15 secs : %s" % time.ctime())

def test_sum():
    print("Verifying 5+5==10")
    assert sum(5, 5) == 10

def test_sum_positive_ok():
    print("Verifying 1+2==4")
    assert sum_only_positive(1, 2) == 4

def test_sum_positive_fail():
    print("Verifying -1+2==None")
    assert sum_only_positive(-1, 2) is None

