import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)