n = 10
print("Powers of 2:", [2**x for x in range(n)])
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")