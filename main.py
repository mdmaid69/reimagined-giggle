import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import unittest

class TestStringMethods(unittest.TestCase):
        def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")