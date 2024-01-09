  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)