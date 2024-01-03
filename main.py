import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)