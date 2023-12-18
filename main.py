import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")