import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks