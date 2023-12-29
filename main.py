  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)