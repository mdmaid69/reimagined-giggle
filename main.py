import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)