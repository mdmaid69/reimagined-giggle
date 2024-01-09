i = 0
while i < 5:
        print(i)
        i += 1
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")