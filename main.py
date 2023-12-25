  import os
  def delete_file(file_name):
        os.remove(file_name)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)