import array
def get_array_as_frozenset(array):
        return frozenset(array)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)