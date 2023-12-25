def is_even(n):
        return n % 2 == 0
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h