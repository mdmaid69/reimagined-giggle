import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"