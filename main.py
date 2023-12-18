  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a