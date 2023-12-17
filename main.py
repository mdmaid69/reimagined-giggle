  import os
  def split_path(path):
        return os.path.split(path)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)