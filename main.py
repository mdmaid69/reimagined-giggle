  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)