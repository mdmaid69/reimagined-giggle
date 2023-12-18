import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)