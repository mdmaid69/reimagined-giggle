  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)