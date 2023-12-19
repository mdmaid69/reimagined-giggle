n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")