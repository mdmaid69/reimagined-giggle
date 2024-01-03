  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)