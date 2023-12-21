import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)