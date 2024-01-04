  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)