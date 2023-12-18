  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)