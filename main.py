n = 10
print("Square numbers:", [x**2 for x in range(n)])
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")