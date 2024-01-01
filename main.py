import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value