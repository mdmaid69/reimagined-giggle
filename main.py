import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)