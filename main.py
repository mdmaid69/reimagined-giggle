import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)