  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)