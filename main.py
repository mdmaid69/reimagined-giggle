  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)