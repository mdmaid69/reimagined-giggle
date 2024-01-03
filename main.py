  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)