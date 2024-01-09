  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)