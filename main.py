  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)