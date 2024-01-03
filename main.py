  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)