  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import collections
def create_priority_queue():
        return collections.deque()