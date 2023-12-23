  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)