  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)