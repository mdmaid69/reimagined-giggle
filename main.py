  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)