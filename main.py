import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")