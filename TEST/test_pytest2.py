from sample_pytest2 import inc

def setup_module(module):
    print("setup_module in action!!!     module:%s" % module.__name__)

def teardown_module(module):
    print("teardown_module closing!!! module:%s" % module.__name__)

def test_equivalence():
    print("Test answer 2 ==5?")
    assert inc(3) == 5