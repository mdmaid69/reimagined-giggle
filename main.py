  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)