  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)