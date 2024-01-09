import collections
def count_elements(iterable):
        return collections.Counter(iterable)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)