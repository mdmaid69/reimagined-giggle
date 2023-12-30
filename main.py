import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)