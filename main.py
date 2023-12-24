  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)