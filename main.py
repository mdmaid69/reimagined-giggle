  import sys
  def get_python_version():
        return sys.version
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)