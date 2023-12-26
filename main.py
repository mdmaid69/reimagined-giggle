  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)