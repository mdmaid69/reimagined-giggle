import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")