  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)