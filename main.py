  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)