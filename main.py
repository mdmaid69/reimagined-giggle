  import os
  def get_current_working_directory():
        return os.getcwd()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)