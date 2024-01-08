import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]