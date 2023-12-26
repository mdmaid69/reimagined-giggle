import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]