  import sys
  def get_python_version():
        return sys.version
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)