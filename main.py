  import os
  def get_current_directory():
        return os.getcwd()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)