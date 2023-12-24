import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns