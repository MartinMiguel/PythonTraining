#py.test -s -v test_pytest4.py
from __future__ import print_function


def resource_a_setup():
    print('resources_a_setup()')

def resource_a_setupC():
    print('resources_Class_setup()')

def resource_a_teardown():
    print('resources_a_teardown()')

def setup_module(module):
    print('\nsetup_module()')
    resource_a_setup()

def teardown_module(module):
    print('\nteardown_module()')
    resource_a_teardown()

#def setup_function(function):
#    print('\nsetup_function()')

#def teardown_function(function):
#    print('\nteardown_function()')

def test_1_that_needs_resource_a():
    print('test_1_that_needs_resource_a()')

def test_2():
    print('-  test_2()')


class TestClass:

    @classmethod
    def setup_class(cls):
        print('\nsetup_class()')
        resource_a_setupC()

    @classmethod
    def teardown_class(cls):
        print('teardown_class()')

    def setup_method(self, method):
        print('\nsetup_method()')

    def teardown_method(self, method):
        print('\nteardown_method()')

    def test_3(self):
        print('- test_3()')

    def test_4(self):
        print('- test_4()')