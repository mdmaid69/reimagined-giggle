import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  def multiply_numbers(x, y):
        return x * y