  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)