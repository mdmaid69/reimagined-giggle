  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)