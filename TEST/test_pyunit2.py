#pyunit framework

import unittest

from sample_pyunit2 import multiply


class TestUM(unittest.TestCase):
    def test_numbers_3_4(self):
        self.assertEqual(multiply(3, 4), 12)