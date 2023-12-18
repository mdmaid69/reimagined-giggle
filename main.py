text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")