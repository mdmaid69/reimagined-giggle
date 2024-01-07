  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable