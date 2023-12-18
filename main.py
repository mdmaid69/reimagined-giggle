import array
def get_array_buffer_info(array):
        return array.buffer_info()
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)