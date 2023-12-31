  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)