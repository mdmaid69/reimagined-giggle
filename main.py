  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)