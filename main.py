import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")