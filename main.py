import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value