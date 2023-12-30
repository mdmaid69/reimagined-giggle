import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")