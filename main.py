import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)