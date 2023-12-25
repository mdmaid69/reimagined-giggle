import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)