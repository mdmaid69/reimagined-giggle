import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  def cube_number(x):
        return x**3