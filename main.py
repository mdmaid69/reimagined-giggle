  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)