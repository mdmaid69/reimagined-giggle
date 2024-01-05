  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)