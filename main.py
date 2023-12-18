  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h