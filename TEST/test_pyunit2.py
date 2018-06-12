#pyunit framework

import unittest

from sample_pyunit2 import multiply

def setup_module(module):
    print("setup_module in action!!!     module:%s" % module.__name__)

def teardown_module(module):
    print("teardown_module closing!!! module:%s" % module.__name__)

class TestUM(unittest.TestCase):
    def test_numbers_3_4(self):
        self.assertEqual(multiply(3, 4), 12)