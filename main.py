import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]