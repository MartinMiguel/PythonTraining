from sample_pytest3 import multiply

def setup_module(module):
    print("setup_module in action!!!     module:%s" % module.__name__)

def teardown_module(module):
    print("teardown_module closing!!! module:%s" % module.__name__)

def setup_function(function):
    print("setup_function    function:%s" % function.__name__)

def teardown_function(function):
    print("teardown_function function:%s" % function.__name__)

def test_numbers_3_4():
    print("Multiply 3*4==12")
    assert multiply(3, 4) == 12

def test_strings_a_3():
    print("Multiply 3*a==aaa")
    assert multiply('a', 3) == 'aaa'