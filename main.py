  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h