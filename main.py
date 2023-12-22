  def add_numbers(x, y):
        return x + y
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h