def find_max(numbers):
        return max(numbers)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h