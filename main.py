  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)