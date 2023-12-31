import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
n = 10
print("Powers of 2:", [2**x for x in range(n)])