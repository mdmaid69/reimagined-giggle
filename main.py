  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)