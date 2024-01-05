import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]