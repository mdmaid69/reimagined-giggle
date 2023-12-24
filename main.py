numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")