import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)