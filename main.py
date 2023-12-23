import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)