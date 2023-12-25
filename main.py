def square_number(x):
        return x**2
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h