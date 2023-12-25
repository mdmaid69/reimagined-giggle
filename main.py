  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import collections
def count_elements(iterable):
        return collections.Counter(iterable)