import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)