  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)