import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))