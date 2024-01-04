import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)