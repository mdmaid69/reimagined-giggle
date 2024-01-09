  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a