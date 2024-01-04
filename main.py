  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)