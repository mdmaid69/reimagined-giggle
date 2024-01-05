  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)