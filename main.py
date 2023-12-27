  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)