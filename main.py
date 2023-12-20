import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])