  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import array
def get_array_slice(array, i, j):
        return array[i:j]