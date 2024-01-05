  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h