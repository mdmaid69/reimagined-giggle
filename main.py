  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)