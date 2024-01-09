  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)