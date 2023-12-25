  def is_even(n):
        return n % 2 == 0
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)