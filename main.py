def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")