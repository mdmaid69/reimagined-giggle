import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))