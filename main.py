import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)