import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)