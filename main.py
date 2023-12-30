  def remove_duplicates(lst):
        return list(set(lst))
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h