import unittest
import inspect


#run as python -m unittest -q test_pyunit3.py
class TestLists(unittest.TestCase):
   #SetUp() / tearDown()` – before and after test methods
    def setUp(self):
        self.logPoint()
        self.myList = [1, 2, 3, 4]

    def test_len(self):
        self.logPoint()
        self.assertEqual(len(self.myList), 4)
        self.myList.append(-1)
        self.assertEqual(len(self.myList), 5)

    def test_min(self):
        self.logPoint()
        self.assertEqual(min(self.myList), 1)

    def tearDown(self):
        self.logPoint()

    def logPoint(self):
        #using the id() method that is part of unittest.TestCase to get the name of the current test
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))