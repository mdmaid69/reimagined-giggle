  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)