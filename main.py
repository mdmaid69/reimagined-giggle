  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a