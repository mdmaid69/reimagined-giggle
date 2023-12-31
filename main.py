  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)