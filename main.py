  import os
  def get_base_name(path):
        return os.path.basename(path)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)