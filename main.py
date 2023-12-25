  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)