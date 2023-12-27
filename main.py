import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))