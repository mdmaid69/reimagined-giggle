def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")