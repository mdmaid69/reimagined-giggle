import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)