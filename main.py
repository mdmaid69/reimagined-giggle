  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)