import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import collections
def create_ordered_dict():
        return collections.OrderedDict()