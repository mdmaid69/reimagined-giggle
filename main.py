import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)