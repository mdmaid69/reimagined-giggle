  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)