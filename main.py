def calculate_area(radius):
        return 3.14 * radius * radius
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")