for i in range(10): print(i)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h