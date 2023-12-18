  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)