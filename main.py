import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value