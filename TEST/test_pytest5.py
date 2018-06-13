#py.test -s -v test_pytest5.py::test_2_that_does_not
#py.test -s -v test_pytest5.py

#Test that shares a resource

from __future__ import print_function
import pytest

#However, you can return anything you want from the fixture function
#Scope module dont print resources
#@pytest.fixture(scope="module")
#Scope is functions
@pytest.fixture(scope='function', params=None, autouse=False)
#def resource_a(request):
#def resource_a():
def resource_a():
    data = {'foo': 1, 'bar': 2, 'baz': 3}
    print('\nresources_a() "setup"')
    return data
#    return None

def test_1_that_needs_resource_a(resource_a):
    print('test_1_that_needs_resource_a()')
    assert resource_a['foo'] == 1

def test_2_that_does_not():
    print('\ntest_2_that_does_not()')


def test_3_that_does(resource_a):
    print('test_3_that_does()')