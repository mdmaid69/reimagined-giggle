import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"