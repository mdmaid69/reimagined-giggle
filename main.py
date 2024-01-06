def convert_to_hex(n):
        return hex(n)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h