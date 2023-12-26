import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)