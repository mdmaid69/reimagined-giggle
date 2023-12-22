  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h