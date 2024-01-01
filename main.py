import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  def calculate_circumference_circle(r):
        return 2 * 3.14 * r