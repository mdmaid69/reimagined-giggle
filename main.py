  import os
  def split_path(path):
        return os.path.split(path)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)