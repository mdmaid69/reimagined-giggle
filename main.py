  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)