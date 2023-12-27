import array
def get_array_as_memoryview(array):
        return memoryview(array)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value