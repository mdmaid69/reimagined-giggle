import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)