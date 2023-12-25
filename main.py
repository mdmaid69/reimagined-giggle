  def count_elements(lst):
        return len(lst)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h