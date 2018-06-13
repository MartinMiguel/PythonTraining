#pyunit framework
#run py.test -s test_pyunit2.py for almost real display

import unittest
import time
import logging

from sample_pyunit2 import multiply, multiply2

logging.basicConfig(level=logging.DEBUG)

def setup_module(module):
    print("setup_module in action!!!     module:%s" % module.__name__)
    #Real time printing
    log = logging.getLogger('setup_module')
    time.sleep(1)
    log.debug('after 1 sec')
    time.sleep(1)
    log.debug('after 2 sec')
    time.sleep(1)
    log.debug('after 3 sec')
    assert 1, 'should pass'

def teardown_module(module):
    print("teardown_module closing!!! module:%s" % module.__name__)
    #Real time printing
    log = logging.getLogger('teardown_module')
    time.sleep(1)
    log.debug('after 1 sec')
    time.sleep(1)
    log.debug('after 2 sec')
    time.sleep(1)
    log.debug('after 3 sec')
    assert 0, 'should pass'

class Test_Mult3_4(unittest.TestCase):
    def test_numbers_3_4(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_numbers_1_4(self):
        self.assertEqual(multiply2(1, 4), 8)

#Allows to run the code just running the file
if __name__ == '__main__':
    unittest.main()