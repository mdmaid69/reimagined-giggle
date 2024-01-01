  import sys
  def get_python_version():
        return sys.version
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h