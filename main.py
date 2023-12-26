import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)