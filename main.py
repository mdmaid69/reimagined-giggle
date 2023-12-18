import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import os
  def get_base_name(path):
        return os.path.basename(path)