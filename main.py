def reverse_string(s):
        return s[::-1]
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h