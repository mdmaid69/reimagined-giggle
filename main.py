def find_max(lst):
        return max(lst)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h