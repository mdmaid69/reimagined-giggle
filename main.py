n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")