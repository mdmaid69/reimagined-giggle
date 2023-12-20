  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)