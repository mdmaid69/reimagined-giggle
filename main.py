import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))