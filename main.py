import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")