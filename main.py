  import math
  def calculate_square_root(n):
        return math.sqrt(n)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h