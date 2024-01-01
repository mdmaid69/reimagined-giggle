import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value