import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
  import os
  def delete_file(file_name):
        os.remove(file_name)