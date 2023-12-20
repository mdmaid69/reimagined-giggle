import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)