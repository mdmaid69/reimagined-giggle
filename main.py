import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)