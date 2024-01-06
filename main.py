  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)