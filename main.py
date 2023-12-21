import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  def calculate_area_triangle(b, h):
        return 0.5 * b * h