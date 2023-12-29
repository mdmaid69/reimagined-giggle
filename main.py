  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)