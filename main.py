import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)