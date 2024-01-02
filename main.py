import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)