  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)