import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h