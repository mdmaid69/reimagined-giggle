import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)