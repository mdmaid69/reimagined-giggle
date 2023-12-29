import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)