  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)