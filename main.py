import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")