text = "Hello, world!"
print("Uppercase:", text.upper())
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")