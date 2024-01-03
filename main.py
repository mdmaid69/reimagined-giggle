  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)