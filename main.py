import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value