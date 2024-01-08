  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)