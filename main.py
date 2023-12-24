import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value