  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)