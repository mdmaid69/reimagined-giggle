  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)