  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)