import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
n = 10
print("Cube numbers:", [x**3 for x in range(n)])