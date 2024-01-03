import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import itertools
print(list(itertools.permutations([1, 2, 3])))