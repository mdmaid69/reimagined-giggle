import array
def get_bytes_from_array(array):
        return array.tobytes()
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value