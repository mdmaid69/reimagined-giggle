  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)