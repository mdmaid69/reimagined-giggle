  def calculate_area_rectangle(l, w):
        return l * w
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h