  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)