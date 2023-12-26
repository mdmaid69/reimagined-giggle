import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)