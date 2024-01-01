  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)