import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize