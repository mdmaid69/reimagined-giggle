print(sum(range(10)))
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h