  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)