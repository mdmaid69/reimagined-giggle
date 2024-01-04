  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a